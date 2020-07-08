import pandas as pd 
import matplotlib.pyplot as plt

libro = "C:\\Users\\Sebastian_Valverde\\Desktop\\Excel tesis\\servi.xlsx"

df= pd.read_excel(libro, header=0, delim_whitespace=True)
#print(df.head())

tabla =  df[["media","humedad","temperatura","fechahora"]]
ax = tabla.plot(x="fechahora", y="temperatura", rot=0)  #temperatura
bx = tabla.plot(x="fechahora", y="humedad", rot=0) #humedad
cx= tabla.plot(x="fechahora", y="media", rot=0) #humedad del suelo
plt.show()

print(tabla)
