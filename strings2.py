msg="""Hello, 
I am writing to say
Hello.
Cole"""
print(msg)
print(msg.find("Hello"))
print(msg.replace("Hello", "Hi"))
print("Hello" in msg)
print("Cole" not in msg)
name="COLE"
color="PURPLE"
msg1="[" + name + "] loves the color " + color + "!"
print(msg1)
msg2=f'[{name.title()}] loves the color {color.lower()}!'
print(msg2)
