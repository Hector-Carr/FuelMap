import requests

def gen_text(middle_data) -> str:
    head = """const map = new maplibregl.Map({
        style: 'https://tiles.openfreemap.org/styles/liberty',
        center: [153, -27.4],
        zoom: 9,
        container: 'map',
    });"""

    tail = """locs.forEach(loc => {
	var popup = new maplibregl.Popup({closeButton: false}).setHTML(loc['msg']);
        var marker = new maplibregl.Marker({className:'Pump', color:loc['colour']}).setLngLat(loc['latlong']).setPopup(popup).addTo(map);
    });"""

    middle = f"""
    const locs = {middle_data}
    """
    #print(str(middle_data))

    return f'{head}\n{middle}\n{tail}'

if __name__ == '__main__':
    print('hello')
    new_text = gen_text([{'latlong': [153, -27.5], 'msg': '<b>HELLLO</b>', 'colour':'#FF0000'}, {'latlong': [153, -27.4], 'msg': ':))', 'colour':'#00FF00'}])

    with open('map.js', 'w') as f:
        f.write(new_text)
    #print(gen_text_small())
