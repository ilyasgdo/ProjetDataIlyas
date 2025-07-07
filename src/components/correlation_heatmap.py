# src/components/correlation_heatmap.py
import plotly.express as px
import pandas as pd
import numpy as np
from dash import html, dcc


def create_correlation_heatmap(df: pd.DataFrame) -> html.Div:
    """
    Crée une carte de corrélation entre les indicateurs économiques principaux
    
    Args:
        df (pd.DataFrame): DataFrame contenant les données filtrées
        
    Returns:
        html.Div: Composant HTML contenant la carte de corrélation
    """
    
    # Sélectionner les indicateurs économiques principaux
    indicators = {
        'DEC_MED18': 'Salaire Médian',
        'DEC_GI18': 'Indice de Gini',
        'DEC_PCHO18': 'Taux de Chômage',
        'DEC_PPEN18': 'Taux de Retraités',
        'DEC_PACT18': 'Taux d\'Activité',
        'DEC_PTSA18': 'Taux de Salariés',
        'DEC_PAUT18': 'Autres Revenus'
    }
    
    # Créer un DataFrame avec seulement les indicateurs sélectionnés
    df_indicators = df[list(indicators.keys())].copy()
    
    # Calculer la matrice de corrélation
    correlation_matrix = df_indicators.corr()
    
    # Renommer les colonnes et index avec les noms lisibles
    correlation_matrix.columns = [indicators[col] for col in correlation_matrix.columns]
    correlation_matrix.index = [indicators[col] for col in correlation_matrix.index]
    
    # Créer le graphique heatmap
    fig = px.imshow(
        correlation_matrix,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu",
        color_continuous_midpoint=0,
        title="Matrice de Corrélation des Indicateurs Économiques",
        labels={
            "x": "Indicateurs",
            "y": "Indicateurs",
            "color": "Corrélation"
        }
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
            title="",
            title_font={"size": 16, "family": "Arial, sans-serif"},
            tickfont={"size": 12, "family": "Arial, sans-serif"},
            tickangle=45
        ),
        yaxis=dict(
            title="",
            title_font={"size": 16, "family": "Arial, sans-serif"},
            tickfont={"size": 12, "family": "Arial, sans-serif"},
        ),
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="white",
        margin=dict(l=100, r=40, t=60, b=100),
        coloraxis_colorbar=dict(
            title="Coefficient de Corrélation",
            title_font={"size": 14, "family": "Arial, sans-serif"},
            tickfont={"size": 12, "family": "Arial, sans-serif"},
        )
    )
    
    # Personnaliser le texte dans les cellules
    fig.update_traces(
        texttemplate="%{z:.2f}",
        textfont={"size": 12, "family": "Arial, sans-serif", "color": "white"}
    )
    
    # Composant HTML contenant le graphique et le texte explicatif
    return html.Div(
        children=[
            html.H3(
                "Matrice de Corrélation des Indicateurs Économiques",
                style={
                    "text-align": "center",
                    "color": "#2c3e50",
                    "margin-bottom": "20px",
                },
            ),
            dcc.Graph(figure=fig),
            html.H4(
                "Cette matrice révèle les relations entre les différents indicateurs économiques. "
                "Les valeurs proches de 1 (rouge) indiquent une forte corrélation positive, "
                "tandis que les valeurs proches de -1 (bleu) indiquent une forte corrélation négative.",
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