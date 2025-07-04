import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.utilities.sql_database import SQLDatabase

# Import agent-based SQL toolkit and agent creation utilities
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

# Load API key from .env
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

def build_sql_chain_from_path(db_path: str):
    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
    )
    return agent_executor


def get_schema_diagram(db_path: str) -> str:
    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
    table_schemas = db.get_table_info().strip().split("\n\n")
    graph = [
        "digraph schema {",
        "node [shape=plaintext fontname=Helvetica];"
    ]

    for table in table_schemas:
        if not table.strip():
            continue
        lines = [line for line in table.strip().splitlines() if line.strip() != ")"]
        parts = lines[0].split()
        if len(parts) < 3 or parts[0].upper() != "CREATE" or parts[1].upper() != "TABLE":
            continue
        table_name = parts[2]
        cols = []
        pk = set()
        fk = set()
        columns = []

        # First pass: collect constraints and columns
        for line in lines[1:]:
            line = line.strip().strip(",")
            if not line:
                continue

            # Table-level primary key
            if line.upper().startswith("PRIMARY KEY"):
                pk_fields = line[line.find("(")+1:line.find(")")].split(",")
                pk.update(field.strip().strip('"') for field in pk_fields)
                continue

            # Table-level foreign key
            if line.upper().startswith("FOREIGN KEY"):
                fk_field = line[line.find("(")+1:line.find(")")].strip().strip('"')
                fk.add(fk_field)
                continue

            columns.append(line)

        # Second pass: generate rows with labels
        for line in columns:
            col_parts = line.split()
            if not col_parts:
                continue
            col_name = col_parts[0].strip('"')

            if "PRIMARY" in line.upper() and "KEY" in line.upper():
                pk.add(col_name)
            if "REFERENCES" in line.upper():
                fk.add(col_name)

            prefix = ""
            if col_name in pk:
                prefix = "[PK] "
            elif col_name in fk:
                prefix = "[FK] "

            cols.append(f"<tr><td align='left'>{prefix}{col_name}</td></tr>")

        graph.append(f"""
        {table_name} [label=<
        <table border="1" cellborder="0" cellspacing="0">
        <tr><td bgcolor="lightblue"><b>{table_name}</b></td></tr>
        {''.join(cols)}
        </table>
        >];
        """)

    graph.append("}")
    return "\n".join(graph)