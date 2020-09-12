import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks", color_codes=True)


def cum_sum_plot(df, col='flight_count', gtype='cum_perc', title='',xlabel='',ylabel='', vert_lines=False, coltype=''):
    df['cum_sum'] = df[col].cumsum()
    if gtype == 'cum_perc':
        df['cum_perc'] = 100*df['cum_sum']/df[col].sum()
    df[gtype].plot(figsize=(9,5))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if vert_lines:
        add_verticals(df, dtype=coltype)
    plt.show()
    
def catplot(df, x=None, y=None, hue=None, kind='strip', order=None, title='' , xlab='', ylab='' , rot=60, color=None, xticklabs=None):
    g = sns.catplot(x=x, y=y, hue=hue, kind=kind, color=color,
            palette="pastel", edgecolor=".6", height=4, aspect=3,
            data=df, order=order)
    g.set_axis_labels(xlab, ylab)
    g.fig.suptitle(title)
    if xticklabs:
        g.set_xticklabels(xticklabs, rotation=rot)
    else:
        g.set_xticklabels(rotation=rot)
    
    
def plot(df, x=None, y=None, hue=None, kind='strip', order=None, title='' , xlab='', ylab='' , rot=60):
    g = sns.lineplot(x=x, y=y, hue=hue, kind=kind,
            palette="pastel", edgecolor=".6", height=4, aspect=3,
            data=df, order=order)
    g.set_axis_labels(xlab, ylab)
    g.fig.suptitle(title) 
    g.set_xticklabels(rotation=rot)
    
    
def add_verticals(df, plot_type=None, dtype=''):
    lines = []
    line_names = []
    cols = ["r","m","g","y"]
    for cov_rate,c in zip([25,50,90,99], cols):
        needed_top_x = df[df.cum_perc <= cov_rate].index.max() +1

        lines.append(plt.axvline( x=needed_top_x, linewidth=1.5, color=c))
        line_name = f"{cov_rate}% {dtype} are covered"
        line_names.append(line_name)
        print(f"{line_name} with most frequent {needed_top_x} locations")
    
    if plot_type == "distrib":
        plt.legend(lines, line_names,loc='lower right', bbox_to_anchor=(0.1, -0.2),
               fancybox=True, shadow=True, ncol=5)
    else:
         plt.legend(lines, line_names,loc='lower right',)
    plt.show()
    
    
def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.1f%s' % (num, ['', ' K', ' M', ' G', ' T', ' P'][magnitude])