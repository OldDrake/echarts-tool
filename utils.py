from pyecharts.charts import Pie, Grid
from pyecharts import options as opts
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot


#data format --> [(key1, value), (key2, value)]
def draw_piechart(data, title, filename):
    piechart = Pie()
    piechart.add("", data, center=["35%", "50%"])
    piechart.set_global_opts(
        title_opts=opts.TitleOpts(title=title),
        legend_opts=opts.LegendOpts(pos_right="25%", item_width=40, item_height=24, orient='vertical'),
    )
    piechart.set_series_opts(
        label_opts=opts.LabelOpts(formatter="{b}: {c}"),
    )
    #piechart.render(filename)
    make_snapshot(snapshot, piechart.render(), filename)

test_data = [('魏', 1), ('蜀', 1), ('吴', 1)]
draw_piechart(test_data, '三国鼎立', 'test.png')