from django.http import JsonResponse
from mysql.connector import Error
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import mysql.connector
import json


@api_view(['GET'])
def database(request):
    d = {}
    if request.method == 'GET':
        try:
            conn = mysql.connector.connect(user="root", password="sonali", host="localhost",
                                           autocommit=True, database='data1')
            print(conn)
            cursor = conn.cursor(buffered=True)
            print(cursor)
            try:
                cursor.execute("select * from user")
                data_obj = cursor.fetchall()
                print(data_obj)
                d["key"] = data_obj
            except Exception as e:
                print(e)
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)
        return JsonResponse({"msg": "successfully connected"})
    return JsonResponse({"msg": "null"})


@api_view(["GET"])
def company_api(request):
    company_dict = {}
    company_dict['ok'] = 'true'
    if request.method == 'GET':
        conn = mysql.connector.connect(user="root", password="sonali", host="localhost",autocommit=True, database='data1')
        cursor = conn.cursor()
        try:
            cursor.execute("select * from user")
            company_obj = cursor.fetchall()
            print(company_obj)
            for x in company_obj:
                cursor.execute('''select * from new_company where username = "%s" ''' %(x[0]))
                comp_obj = cursor.fetchone()
                print(comp_obj)
                cursor.execute('''select * from new_company_agent where new_company="%s";''' %(comp_obj[0]))
                for y in company_obj:
                    agent_dict = {}
                    agent_dict["company_agent_name"] = y[1]
                    agent_dict["created_date"] = y[2]
                    agent_dict["no_of_call_attended"] = y[3]
                    agent_dict["total_time_spent_for_call_attended"] = y[4]
                    agent_list = []
                    for z in company_obj:
                        agent_list.append(agent_dict)
                    company_dict = {}
                    company_dict["username"] = z[0]
                    company_dict["brand_name"] = comp_obj[1]
                    company_dict["first_name"] = z[1]
                    company_dict["last_name"] = z[2]
                    company_dict["agent"] = agent_list

                    company_list = []
                    for x in company_obj:
                        company_list.append(company_dict)
                        company_dict["Companies"] = company_list
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)
            # jsonStr = json.dumps(company_dict, indent=2)
            # print(jsonStr)
        return JsonResponse(company_dict)
    return JsonResponse({"msg": "null"})

