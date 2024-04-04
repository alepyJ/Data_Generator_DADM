import pandas as pd


def generate_competicion_disciplina():
    torneo_data = {
        'Competicion': [
            'Torneo Internacional de Atletismo', 'Campeonato Nacional de Atletismo', 'Copa de Primavera de Atletismo',
            'Liga Premier de Fútbol', 'Copa Mundial de Fútbol', 'Eurocopa de Fútbol',
            'Campeonato Mundial de Halterofilia', 'Open Internacional de Halterofilia',
            'Torneo de Otoño de Fútbol', 'Copa de Clubes de Fútbol', 'Torneo Universitario de Fútbol',
            'Campeonato Interescolar de Atletismo', 'Maratón Internacional', 'Copa de Atletismo Indoor'
        ],
        'Disciplina': [
            'Atletismo 100m', 'Atletismo 100m', 'Atletismo 100m',
            'Fútbol 11', 'Fútbol 11', 'Fútbol 11',
            'Halterofilia 2 tiempos', 'Halterofilia 2 tiempos',
            'Fútbol 11', 'Fútbol 11', 'Fútbol 11',
            'Atletismo 100m', 'Atletismo 100m', 'Atletismo 100m'
        ]
    }


    torneo_df = pd.DataFrame(torneo_data)
    torneo_df.to_csv('Competicion-Disciplina.csv', index=False)
    
if __name__ == 'main':
    generate_competicion_disciplina()
