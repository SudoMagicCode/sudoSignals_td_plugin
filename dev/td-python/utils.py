from datetime import datetime


def parDataBlock(par, group=False):
    # placeholder solution for sending pars that are ops
    op_pars = ['OP', 'COMP', 'TOP', 'CHOP', 'SOP', 'MAT', 'DAT']

    if par.style in op_pars:
        par_style = 'Str'
        value = str(par.eval())
    else:
        par_style = par.style
        value = par.eval()

    dataBlock = {
        "name": par.name,
        "label": par.label,
        "path": par.owner.path,
        "style": par_style,
        "index": par.index,
        "currentValue": value,
        "inGroup": group,
    }
    if (par.style == "Menu" or par.style == "StrMenu"):
        dataBlock['menuLabels'] = par.menuLabels
        dataBlock['menuNames'] = par.menuNames
    return dataBlock


def groupDataBlock(group):
    if (len(group) > 1):
        return {
            "group": True,
            "name": group[0].name,
            "label": group[0].label,
            "style": group[0].style,
            "index": group[0].index,
            "path": group[0].owner.path,
            "pars": [parDataBlock(par, group=True) for par in group]
        }
    else:
        return parDataBlock(group[0], group=False)


def CreateAllParDataBlocks(page):
    parsData = []
    groups = page.parTuplets
    for g in groups:
        parsData.append(groupDataBlock(g))
    return parsData


def GetLogTimeStamp() -> str:
    return datetime.now().isoformat(' ', 'seconds')


def TextPortMsg(level: str, msg: str) -> str:
    return f'{GetLogTimeStamp()} [*] SUDOSIGNALS :: {level} :: {msg}'
