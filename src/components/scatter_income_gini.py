# src/components/scatter_income_gini.py
import plotly.express as px
import pandas as pd
from dash import html, dcc


def create_scatter_income_gini(df: pd.DataFrame) -> html.Div:
    """
    Crée un graphique de dispersion montrant la relation entre le salaire médian et l'indice de Gini
    
    Args:
        df (pd.DataFrame): DataFrame contenant les données filtrées
        
    Returns:
        html.Div: Composant HTML contenant le graphique de dispersion
    """
    
    # Créer le graphique de dispersion
    fig = px.scatter(
        df,
        x="DEC_MED18",
        y="DEC_GI18",
        color="DEC_PCHO18",  # Couleur basée sur le taux de chômage
        size="DEC_PIMP18",   # Taille basée sur le nombre de ménages fiscaux
        hover_data=["LIBCOM", "LIBIRIS", "DEC_PCHO18", "DEC_PPEN18"],
        labels={
            "DEC_MED18": "Salaire Médian (€)",
            "DEC_GI18": "Indice de Gini",
            "DEC_PCHO18": "Taux de Chômage (%)",
            "DEC_PIMP18": "Nombre de Ménages Fiscaux"
        },
        title="Relation entre Salaire Médian et Inégalités (Indice de Gini)",
        color_continuous_scale="RdYlBu_r"
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
            title="Salaire Médian (€)",
            title_font={"size": 16, "family": "Arial, sans-serif"},
            tickfont={"size": 14, "family": "Arial, sans-serif"},
        ),
        yaxis=dict(
            title="Indice de Gini",
            title_font={"size": 16, "family": "Arial, sans-serif"},
            tickfont={"size": 14, "family": "Arial, sans-serif"},
        ),
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="white",
        margin=dict(l=40, r=40, t=60, b=40),
        coloraxis_colorbar=dict(
            title="Taux de Chômage (%)",
            title_font={"size": 14, "family": "Arial, sans-serif"},
        )
    )
    
    # Composant HTML contenant le graphique et le texte explicatif
    return html.Div(
        children=[
            html.H3(
                "Relation entre Salaire Médian et Inégalités (Indice de Gini)",
                style={
                    "text-align": "center",
                    "color": "#2c3e50",
                    "margin-bottom": "20px",
                },
            ),
            dcc.Graph(figure=fig),
            html.H4(
                "Les zones avec des salaires médians plus élevés tendent à avoir des inégalités moins importantes. "
                "La taille des bulles représente le nombre de ménages fiscaux et la couleur le taux de chômage.",
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