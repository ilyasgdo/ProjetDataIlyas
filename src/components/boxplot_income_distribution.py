# src/components/boxplot_income_distribution.py
import plotly.express as px
import pandas as pd
from dash import html, dcc


def create_boxplot_income_distribution(df: pd.DataFrame) -> html.Div:
    """
    Crée un graphique en boîte montrant la distribution des salaires médians par département
    
    Args:
        df (pd.DataFrame): DataFrame contenant les données filtrées
        
    Returns:
        html.Div: Composant HTML contenant le graphique en boîte
    """
    
    # Extraire le code département des communes (2 premiers caractères du code commune)
    df_copy = df.copy()
    df_copy['DEPARTEMENT'] = df_copy['COM'].astype(str).str[:2]
    
    # Mapper les codes département aux noms
    dept_names = {
        '75': 'Paris',
        '77': 'Seine-et-Marne',
        '78': 'Yvelines', 
        '91': 'Essonne',
        '92': 'Hauts-de-Seine',
        '93': 'Seine-Saint-Denis',
        '94': 'Val-de-Marne',
        '95': 'Val-d\'Oise'
    }
    
    df_copy['DEPARTEMENT_NOM'] = df_copy['DEPARTEMENT'].map(dept_names).fillna('Autre')
    
    # Créer le graphique en boîte
    fig = px.box(
        df_copy,
        x="DEPARTEMENT_NOM",
        y="DEC_MED18",
        title="Distribution des Salaires Médians par Département",
        labels={
            "DEC_MED18": "Salaire Médian (€)",
            "DEPARTEMENT_NOM": "Département"
        },
        color="DEPARTEMENT_NOM",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    # Personnaliser l'apparence
    fig.update_layout(
        title={
            "text": "",
            "x": 0.5,
            "xanchor": "center",
            "font": {"size": 20, "family": "Arial, sans-serif", "color": "#2c3e50"},
        },
        xaxis=dict(
            title="Département",
            title_font={"size": 16, "family": "Arial, sans-serif"},
            tickfont={"size": 14, "family": "Arial, sans-serif"},
            tickangle=45
        ),
        yaxis=dict(
            title="Salaire Médian (€)",
            title_font={"size": 16, "family": "Arial, sans-serif"},
            tickfont={"size": 14, "family": "Arial, sans-serif"},
        ),
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="white",
        margin=dict(l=40, r=40, t=60, b=80),
        showlegend=False
    )
    
    # Composant HTML contenant le graphique et le texte explicatif
    return html.Div(
        children=[
            html.H3(
                "Distribution des Salaires Médians par Département",
                style={
                    "text-align": "center",
                    "color": "#2c3e50",
                    "margin-bottom": "20px",
                },
            ),
            dcc.Graph(figure=fig),
            html.H4(
                "Les boîtes montrent la distribution des salaires médians dans chaque département. "
                "Les points aberrants révèlent des zones avec des revenus exceptionnellement élevés ou faibles.",
                style={
                    "text-align": "center",
                    "color": "#2c3e50",
                    "margin-top": "20px",
                    "font-size": "14px",
                    "font-style": "italic",
                },
            ),
        ],
        style={
            "padding": "20px",
            "background-color": "#ecf0f1",
            "border-radius": "10px",
            "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
            "max-width": "900px",
            "margin": "0 auto",
        },
    )