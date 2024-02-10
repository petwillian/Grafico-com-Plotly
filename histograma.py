
import plotly.express as px
import plotly.io as io
import numpy as np

pesquisa = np.random.normal(170, 10, 250)

fig = px.histogram(pesquisa, nbins=8, title='Titulo do Gráfico')

#fig.update_layout(showlegend=False) # tira a lengenda ao lado do gráfico

fig.update_xaxes(title='Label X')
fig.update_yaxes(title='Label Y')

fig.update_traces(marker_line_width=0.5, marker_line_color='#ffffff')

#io.write_image(fig , 'histograma.png')

fig.show()
