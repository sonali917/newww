# to show company_details
agent_dict = {}
agent_dict["company_agent_name"] = "y.company_agent_name"
agent_dict["created_date"] = "y.created_date"
agent_dict["no_of_call_attended"] = "y.call_attended"
agent_dict["total_time_spent_for_call_attended"] = "y.total_time"
agent_list = []
for y in agent_obj_list:
    agent_list.append(agent_dict)
company_dict = {}
company_dict["username"] = "x.username"
company_dict["brand_name"] = "x.brand_name"
company_dict["first_name"] = "x.brand_name"
company_dict["last_name"] = "x.last_name"
company_dict["agent"] = agent_list

company_list = []
for x in company_obj_list:
    company_list.append(company_dict)
    d = {}
    d['ok'] = 'true'
    d["Companies"] = company_list

company_dict["username"] = x[0]
company_dict["brand_name"] = comp_obj[1]
company_dict["first_name"] = x[1]
company_dict["last_name"] = x[2]
company_dict["agent"] = agent_list






# to create user wise company data
agentss_dict = {}
agentss_dict["company_agent_name"] = "z.company_agent_name"
agentss_dict["created_date"] = "z.created_date"
agentss_dict["no_of_call_attended"] = "z.no_of_calls_attended"
agentss_dict["total_time_spent_for_call_attended"] = "z.total_time_spent_for_call_attended"

agentss_list =[]
for z in agentss_obj_list:
    agentss_list.append(agentss_dict)
user_dict = {}
user_dict["result"]: "true"
user_dict["status"]: 200
user_dict["username"]: "x.username"
user_dict["brand_name"]: "x.brand_name"
user_dict["first_name"]: "x.first_name"
user_dict["last_name"]: "x.last_name"
user_dict["agent"]: agentss_list

#

mydb=mysql.connector.connect(host='localhost',user='root',password='vinay@mysql777',database='api_database',auth_plugin='mysql_native_password')
            cursor = mydb.cursor(buffered=True)
            return_dict={}
            return_dict.update({"ok":True})
            return_dict.update({"Companies":[]})
            try:
               sql_statement="SELECT * from user"
               cursor.execute(sql_statement)
               for sql_data in cursor.fetchall():
                    company_sql_statement='''select * from Company where user_name = "%s" '''%(sql_data[0])
                    print("company_sql_statement===>",company_sql_statement)
                    cursor.execute(company_sql_statement)
                    comp_obj=cursor.fetchone()
                    agent_sql_statement='''select * from agent where company="%s";'''%(comp_obj[0])
                    cursor.execute(agent_sql_statement)
                    for agent_obj in cursor.fetchall():
                       print(agent_obj[0])
                       print(agent_obj[1])
                       print(agent_obj[2])
                       print(agent_obj[3])
                       print(agent_obj[4])
                       print(agent_obj[5])
            except Exception as e:
               print(e)
            cursor.close()
            mydb.close()