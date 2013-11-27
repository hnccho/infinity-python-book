#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hangulize import hangulize

clubs = {
    u'Futbol Club Barcelona': 'cat',
    u'Real Madrid Club de Fútbol': 'spa',
    u'València Club de Futbol': 'spa',
    u'Villarreal Club de Fútbol, S.A.D.': 'spa',
    u'Athletic Club': 'spa',
    u'Sevilla Fútbol Club S.A.D.': 'spa',
    u'Club Atlético de Madrid S.A.D.': 'spa',
    u'Reial Club Deportiu Espanyol de Barcelona': 'spa',
    u'Real Racing Club de Santander': 'spa',
    u'Málaga Club de Fútbol': 'spa',
    u'Real Club Deportivo Mallorca': 'spa',
    u'Levante Unión Deportiva': 'spa',
    u'Real Sociedad': 'spa',
    u'Club Atlético Osasuna': 'spa',
    u'Real Sporting de Gijón': 'spa',
    u'Club Atlético Osasuna': 'spa',
    u'Real Zaragoza': 'spa',
    u'Real Betis Balompié': 'spa',
    u'Rayo Vallecano de Madrid, S.A.D.': 'spa'
    }
    
for name, lang in clubs.iteritems():
    print('%s(%s)' % (name, hangulize(name, lang)))
