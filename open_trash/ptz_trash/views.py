from django.shortcuts import render
import folium
from folium import plugins

def index(request):
    return render(request, "1.html")


def map1():
    m = folium.Map(location=[61.78491, 34.34691], zoom_start=12)
    figure = folium.FeatureGroup(name = "Все ПЭТ мусорки")
    m.add_child(figure)

    group1 = plugins.FeatureGroupSubGroup(figure, "ПЭТ мусорки")
    m.add_child(group1)

    group2 = plugins.FeatureGroupSubGroup(figure, "Сбормобиль")
    m.add_child(group2)

    folium.Marker(
        location = [61.76033, 34.43718],
        popup = "ПЭТ мусорка на ключевой",
        icon = folium.Icon(color="red", icon="trash")
    ).add_to(group1)

    folium.Marker(
        location = [61.78848, 34.34818],
        popup= "ПЭТ мусорка в парке 50-Летия Пионерской Организации",
        icon=folium.Icon(color="red", icon="trash")
    ).add_to(group1)

    folium.Marker(
        location = [61.78497, 34.36438],
        popup= "ПЭТ мусорка в Губернаторском парке возле баскетбольной площадки",
        icon=folium.Icon(color="red", icon="trash")
    ).add_to(group1)

    folium.Marker(
        location = [61.78605, 34.36837],
        popup= "ПЭТ мусорка около разводного моста",
        icon=folium.Icon(color="red", icon="trash")
    ).add_to(group1)

    folium.LayerControl(collapsed=False).add_to(m)
    m.save('ptz_trash/templates/1.html')
