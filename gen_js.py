import requests

def gen_text(middle_data):
    head = """const map = new maplibregl.Map({
        style: 'https://tiles.openfreemap.org/styles/liberty',
        center: [153, -27.4],
        zoom: 9,
        container: 'map',
    });"""

    tail = """locs.forEach(loc => {
        var marker = new maplibregl.Marker().setLngLat(loc['latlong']).addTo(map);
    });"""

    middle = f"""
    const locs = {middle_data}
    """
    #print(str(middle_data))

    return f'{head}\n{middle}\n{tail}'

def gen_text_small():
    head = "const map = new maplibregl.Map({style:'https://tiles.openfreemap.org/styles/liberty',center:[153,-27.4],zoom:9,container:'map',});"
    tail = "locs.forEach(loc=>{var marker = new maplibregl.Marker().setLngLat(loc['latlong']).addTo(map);});"

    return f'{head}{tail}'

if __name__ == '__main__':
    print('hello')
    new_text = gen_text([{'latlong':[153, -27.5]},{'latlong':[153, -27.4]}])

    with open('map.js', 'w') as f:
        f.write(new_text)
    #print(gen_text_small())
