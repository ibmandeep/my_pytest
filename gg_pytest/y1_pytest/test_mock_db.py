import sqlite3

def save_user(name, age):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()




def test_save_user(mocker):
    mock_conn = mocker.patch("sqlite3.connect")

    mock_cursor = mock_conn.return_value.cursor.return_value

    save_user("Singh", 32)

    mock_conn.assert_called_once_with("users.db")
    mock_cursor.execute.assert_called_once_with("INSERT INTO users (name, age) VALUES (?, ?)", ("Singh", 32))