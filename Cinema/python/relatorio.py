import mysql.connector
 
def gerar_relatorio():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cinema_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservas")
    for reserva in cursor.fetchall():
        print(f"Cliente: {reserva[1]}, Sessão: {reserva[2]}, Ingressos: {reserva[3]}")
 
    conn.close()
 
if __name__ == "__main__":
    gerar_relatorio()