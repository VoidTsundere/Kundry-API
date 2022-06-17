#import engine
import json
FORMAT = 'utf-8'

def Get_test():
    msg = "Test successful!"
    return str(len(msg.encode(FORMAT))), msg

def Post_test(data):
    msg = {"code":"success","msg":"Test successful!"}
    
    return str(len(json.dumps(msg).encode(FORMAT))), json.dumps(msg)

commands = {"!GET_TEST":Get_test,
            "!POST_TEST":Post_test}
