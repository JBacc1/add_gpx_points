Script basique d'insertion de points sur une trace gpx. Par défaut tous les "100m lat-lon", soit environ 100m en Nord-Sud, de l'ordre de 65m en Est-Ouest en France (ce choix permet de requérir uniquement gpxpy en paquet supplémentaire.)

Requis : Python 3 + gpxpy (pip install gpxpy)

Usage : python add_gpx_points.py fichier.gpx, ou pour préciser la distance entre deux points (exemple 50m) : python add_gpx_points.py fichier.gpx 50