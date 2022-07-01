#import engine
import json
FORMAT = 'utf-8'
HEADER = 64

def Get_test():
    msg = "Test successful!"
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    
    return send_lenght, msg

def Post_test(data):
    msg = {"code":"success","msg":"Test successful!"}
    
    return str(len(json.dumps(msg).encode(FORMAT))), json.dumps(msg)

commands = {"!GET_TEST":Get_test,
            "!POST_TEST":Post_test}
