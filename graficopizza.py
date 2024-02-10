
import plotly.express as px
import pandas as pd
import plotly.io as io

dados = {'frutas': ['Laranja', 'Melancia', 'Manga', 'Jaca'],
         'porcentagem': [15, 30, 45, 10]
        }
df = pd.DataFrame(data=dados)

fig = px.pie(df, values='porcentagem', names='frutas')

#fig.update_layout(showlegend=False) # tira a lengenda ao lado do gráfico

fig.update_traces(textinfo='percent+label')

fig.update_layout(hovermode=False)# passa o mause encima a apresenta a porcentagem

#io.write_image(fig , 'graficopizza.png')

fig.show()
