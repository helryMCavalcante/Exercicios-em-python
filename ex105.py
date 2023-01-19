def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa!'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel!'
        else:
            r['situação'] = 'Ruim!'
    return r

resp = notas(2.5, 2.5, 2,8.5,sit=True)
print(resp)