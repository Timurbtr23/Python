#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import lyricsgenius
import api_key
from random import randint

LyricsGenius = lyricsgenius.Genius(api_key.client_access_token)


class Rapper:
    analize_count = 5

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    @staticmethod
    def create_lyrics_file():
        with open("lyrics_data.txt", "w", encoding='utf-8') as lyrics_file:
            artist = LyricsGenius.search_artist(input(), max_songs=30)
            for song in artist.songs:
                lyrics_file.write(song.lyrics)

    def collect(self):
        self.sequence = ' ' * self.analize_count
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for char in line:
            if char.isalnum() or char == " ":
                if self.sequence in self.stat:
                    if char in self.stat[self.sequence]:
                        self.stat[self.sequence][char] += 1
                    else:
                        self.stat[self.sequence][char] = 1
                else:
                    self.stat[self.sequence] = {char: 1}
                self.sequence = self.sequence[1:] + char

    def prepare(self):
        self.totals = {}
        self.stat_for_generate = {}
        for sequence, char_stat in self.stat.items():
            self.totals[sequence] = 0
            self.stat_for_generate[sequence] = []
            for char, count in char_stat.items():
                self.totals[sequence] += count
                self.stat_for_generate[sequence].append([count, char])
                self.stat_for_generate[sequence].sort(reverse=True)

    def chat(self, N, out_file_name=None):
        printed = 0
        if out_file_name is not None:
            file = open(out_file_name, 'w', encoding='utf8')
        else:
            file = None

        sequence = ' ' * self.analize_count
        spaces_printed = 0
        while printed < N:
            char = self._get_char(char_stat=self.stat_for_generate[sequence], total=self.totals[sequence])
            if file:
                file.write(char)
            else:
                print(char, end='')
            if char == ' ':
                spaces_printed += 1
                if spaces_printed >= 5:
                    if file:
                        file.write('\n')
                    else:
                        print()
                    spaces_printed = 0
            printed += 1
            sequence = sequence[1:] + char
        if file:
            file.close()

    def _get_char(self, char_stat, total):
        dice = randint(1, total)
        pos = 0
        for count, char in char_stat:
            pos += count
            if dice <= pos:
                break
        return char


rapper = Rapper(file_name='lyrics_data.txt')
rapper.create_lyrics_file()
rapper.collect()
rapper.prepare()
rapper.chat(N=700, out_file_name='rap.txt')
