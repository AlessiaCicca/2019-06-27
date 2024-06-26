from database.DB_connect import DBConnect
from model.connessione import Connessione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getReati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct e.offense_category_id as reato 
from events e """

        cursor.execute(query)

        for row in cursor:
            result.append(row["reato"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getMesi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct month(e.reported_date ) as mese 
from events e 
order by month(e.reported_date )"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["mese"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(categoria,mese):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct e.offense_type_id as tipo
from events e 
where month(e.reported_date) =%s
and e.offense_category_id =%s"""

        cursor.execute(query,(mese,categoria,))

        for row in cursor:
            result.append(row["tipo"])

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getConnessioni(mese,reato):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select  t1.t1 as v1,t2.t2 as v2, count(distinct t1.q1) as peso
    from (select distinct e.offense_type_id as t1,e.neighborhood_id as q1
    from events e 
    where month(e.reported_date) =%s
    and e.offense_category_id =%s) as t1,
    (select distinct e.offense_type_id as t2,e.neighborhood_id as q2
    from events e 
    where month(e.reported_date) =%s
    and e.offense_category_id =%s) as t2
    where t1.t1<t2.t2 and t1.q1=t2.q2
    group by t1.t1,t2.t2
     """

        cursor.execute(query,(mese,reato,mese,reato,))

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result
