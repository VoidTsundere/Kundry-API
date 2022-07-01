using System;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
 
var ipy = Python.CreateRuntime();
dynamic connection = ipy.UseFile("../client.py");

Console.WriteLine(connection.Send_get("!GET_TEST"));
Console.WriteLine(connection.Send_post("!POST_TEST", "DERE"));
connection.Send_get("!DISCONNECT");