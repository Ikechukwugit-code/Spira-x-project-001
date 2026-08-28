from database import get_connection

def test_database_connection():
    connection = get_connection(":memory:")
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS test_table")
    cursor.execute(
        """
        CREATE TABLE test_table(
        id INTEGER PRIMARY KEY,
        name TEXT
        )
        """
    )

    cursor.execute(
        "INSERT INTO test_table (name) VALUES (?)",
        ("SPIRA-X",)
    )
    connection.commit()

    cursor.execute("SELECT name FROM test_table")
    row = cursor.fetchone()

    assert row is not None
    assert row[0] == "SPIRA-X"

    connection.close()