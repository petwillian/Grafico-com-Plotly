
import plotly.express as px
import plotly.io as io

frutas = ['Laranja', 'Melancia', 'Manga', 'Jaca']
quantidades = [60, 100, 85, 30]

fig = px.bar(x=frutas, y=quantidades, title='Titulo do Gráfico', color=frutas, 
             labels=dict(y='Label Y', x='Label X', color='Frutas'))

#io.write_image(fig , 'graficobarra.png' )

fig.show()
