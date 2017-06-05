ldc i 0
mst 0
cup 0 mainFunc
hlt
compareIntegersFunc:
ssp 7
lod i 0 5
lod i 0 6
equ i
fjp compareIntegers0
ldc c 84
out c
ldc c 104
out c
ldc c 101
out c
ldc c 32
out c
ldc c 103
out c
ldc c 105
out c
ldc c 118
out c
ldc c 101
out c
ldc c 110
out c
ldc c 32
out c
ldc c 105
out c
ldc c 110
out c
ldc c 116
out c
ldc c 101
out c
ldc c 103
out c
ldc c 101
out c
ldc c 114
out c
ldc c 115
out c
ldc c 32
out c
ldc c 97
out c
ldc c 114
out c
ldc c 101
out c
ldc c 32
out c
ldc c 116
out c
ldc c 104
out c
ldc c 101
out c
ldc c 32
out c
ldc c 115
out c
ldc c 97
out c
ldc c 109
out c
ldc c 101
out c
ldc c 10
out c
ldc i 32
sro i 0
ujp compareIntegers1
compareIntegers0:
compareIntegers1:
lod i 0 5
lod i 0 6
neq i
fjp compareIntegers2
ldc c 84
out c
ldc c 104
out c
ldc c 101
out c
ldc c 32
out c
ldc c 103
out c
ldc c 105
out c
ldc c 118
out c
ldc c 101
out c
ldc c 110
out c
ldc c 32
out c
ldc c 105
out c
ldc c 110
out c
ldc c 116
out c
ldc c 101
out c
ldc c 103
out c
ldc c 101
out c
ldc c 114
out c
ldc c 115
out c
ldc c 32
out c
ldc c 97
out c
ldc c 114
out c
ldc c 101
out c
ldc c 32
out c
ldc c 110
out c
ldc c 111
out c
ldc c 116
out c
ldc c 32
out c
ldc c 116
out c
ldc c 104
out c
ldc c 101
out c
ldc c 32
out c
ldc c 115
out c
ldc c 97
out c
ldc c 109
out c
ldc c 101
out c
ldc c 10
out c
ldc i 36
sro i 0
ujp compareIntegers3
compareIntegers2:
compareIntegers3:
retp
compareFloatsFunc:
ssp 7
lod r 0 5
lod r 0 6
equ r
fjp compareFloats0
ldc c 84
out c
ldc c 104
out c
ldc c 101
out c
ldc c 32
out c
ldc c 103
out c
ldc c 105
out c
ldc c 118
out c
ldc c 101
out c
ldc c 110
out c
ldc c 32
out c
ldc c 102
out c
ldc c 108
out c
ldc c 111
out c
ldc c 97
out c
ldc c 116
out c
ldc c 115
out c
ldc c 32
out c
ldc c 97
out c
ldc c 114
out c
ldc c 101
out c
ldc c 32
out c
ldc c 116
out c
ldc c 104
out c
ldc c 101
out c
ldc c 32
out c
ldc c 115
out c
ldc c 97
out c
ldc c 109
out c
ldc c 101
out c
ldc c 10
out c
ldc i 30
sro i 0
ujp compareFloats1
compareFloats0:
compareFloats1:
lod r 0 5
lod r 0 6
neq r
fjp compareFloats2
ldc c 84
out c
ldc c 104
out c
ldc c 101
out c
ldc c 32
out c
ldc c 103
out c
ldc c 105
out c
ldc c 118
out c
ldc c 101
out c
ldc c 110
out c
ldc c 32
out c
ldc c 102
out c
ldc c 108
out c
ldc c 111
out c
ldc c 97
out c
ldc c 116
out c
ldc c 115
out c
ldc c 32
out c
ldc c 97
out c
ldc c 114
out c
ldc c 101
out c
ldc c 32
out c
ldc c 110
out c
ldc c 111
out c
ldc c 116
out c
ldc c 32
out c
ldc c 116
out c
ldc c 104
out c
ldc c 101
out c
ldc c 32
out c
ldc c 115
out c
ldc c 97
out c
ldc c 109
out c
ldc c 101
out c
ldc c 10
out c
ldc i 34
sro i 0
ujp compareFloats3
compareFloats2:
compareFloats3:
retp
compareCharactersFunc:
ssp 7
lod c 0 5
lod c 0 6
equ c
fjp compareCharacters0
ldc c 84
out c
ldc c 104
out c
ldc c 101
out c
ldc c 32
out c
ldc c 103
out c
ldc c 105
out c
ldc c 118
out c
ldc c 101
out c
ldc c 110
out c
ldc c 32
out c
ldc c 99
out c
ldc c 104
out c
ldc c 97
out c
ldc c 114
out c
ldc c 97
out c
ldc c 99
out c
ldc c 116
out c
ldc c 101
out c
ldc c 114
out c
ldc c 115
out c
ldc c 32
out c
ldc c 97
out c
ldc c 114
out c
ldc c 101
out c
ldc c 32
out c
ldc c 116
out c
ldc c 104
out c
ldc c 101
out c
ldc c 32
out c
ldc c 115
out c
ldc c 97
out c
ldc c 109
out c
ldc c 101
out c
ldc c 10
out c
ldc i 34
sro i 0
ujp compareCharacters1
compareCharacters0:
ldc c 84
out c
ldc c 104
out c
ldc c 101
out c
ldc c 32
out c
ldc c 103
out c
ldc c 105
out c
ldc c 118
out c
ldc c 101
out c
ldc c 110
out c
ldc c 32
out c
ldc c 99
out c
ldc c 104
out c
ldc c 97
out c
ldc c 114
out c
ldc c 97
out c
ldc c 99
out c
ldc c 116
out c
ldc c 101
out c
ldc c 114
out c
ldc c 115
out c
ldc c 32
out c
ldc c 97
out c
ldc c 114
out c
ldc c 101
out c
ldc c 32
out c
ldc c 110
out c
ldc c 111
out c
ldc c 116
out c
ldc c 32
out c
ldc c 116
out c
ldc c 104
out c
ldc c 101
out c
ldc c 32
out c
ldc c 115
out c
ldc c 97
out c
ldc c 109
out c
ldc c 101
out c
ldc c 10
out c
ldc i 38
sro i 0
compareCharacters1:
retp
mainFunc:
ssp 12
ldc c 0
str c 0 5
ldc c 80
out c
ldc c 114
out c
ldc c 101
out c
ldc c 115
out c
ldc c 115
out c
ldc c 32
out c
ldc c 105
out c
ldc c 32
out c
ldc c 102
out c
ldc c 111
out c
ldc c 114
out c
ldc c 32
out c
ldc c 105
out c
ldc c 110
out c
ldc c 116
out c
ldc c 101
out c
ldc c 103
out c
ldc c 101
out c
ldc c 114
out c
ldc c 32
out c
ldc c 99
out c
ldc c 111
out c
ldc c 109
out c
ldc c 112
out c
ldc c 97
out c
ldc c 114
out c
ldc c 105
out c
ldc c 115
out c
ldc c 111
out c
ldc c 110
out c
ldc c 44
out c
ldc c 32
out c
ldc c 102
out c
ldc c 32
out c
ldc c 102
out c
ldc c 111
out c
ldc c 114
out c
ldc c 32
out c
ldc c 102
out c
ldc c 108
out c
ldc c 111
out c
ldc c 97
out c
ldc c 116
out c
ldc c 32
out c
ldc c 99
out c
ldc c 111
out c
ldc c 109
out c
ldc c 112
out c
ldc c 97
out c
ldc c 114
out c
ldc c 105
out c
ldc c 115
out c
ldc c 111
out c
ldc c 110
out c
ldc c 32
out c
ldc c 97
out c
ldc c 110
out c
ldc c 100
out c
ldc c 32
out c
ldc c 99
out c
ldc c 32
out c
ldc c 102
out c
ldc c 111
out c
ldc c 114
out c
ldc c 32
out c
ldc c 99
out c
ldc c 104
out c
ldc c 97
out c
ldc c 114
out c
ldc c 97
out c
ldc c 99
out c
ldc c 116
out c
ldc c 101
out c
ldc c 114
out c
ldc c 32
out c
ldc c 99
out c
ldc c 111
out c
ldc c 109
out c
ldc c 112
out c
ldc c 97
out c
ldc c 114
out c
ldc c 105
out c
ldc c 115
out c
ldc c 111
out c
ldc c 110
out c
ldc c 58
out c
ldc c 10
out c
ldc i 87
sro i 0
lda 0 5
in c
sto c
ldc i 1
sro i 0
lod c 0 5
ldc c 'c'
equ c
fjp main0
ldc c 0
str c 0 6
ldc c 0
str c 0 7
ldc c 70
out c
ldc c 105
out c
ldc c 114
out c
ldc c 115
out c
ldc c 116
out c
ldc c 32
out c
ldc c 99
out c
ldc c 104
out c
ldc c 97
out c
ldc c 114
out c
ldc c 97
out c
ldc c 99
out c
ldc c 116
out c
ldc c 101
out c
ldc c 114
out c
ldc c 58
out c
ldc c 32
out c
lda 0 6
in c
sto c
ldc i 18
sro i 0
ldc c 83
out c
ldc c 101
out c
ldc c 99
out c
ldc c 111
out c
ldc c 110
out c
ldc c 100
out c
ldc c 32
out c
ldc c 99
out c
ldc c 104
out c
ldc c 97
out c
ldc c 114
out c
ldc c 97
out c
ldc c 99
out c
ldc c 116
out c
ldc c 101
out c
ldc c 114
out c
ldc c 58
out c
ldc c 32
out c
lda 0 7
in c
sto c
ldc i 19
sro i 0
mst 1
lod c 0 6
lod c 0 7
cup 2 compareCharactersFunc
ujp main1
main0:
main1:
lod c 0 5
ldc c 'i'
equ c
fjp main2
ldc i 0
str i 0 8
ldc i 0
str i 0 9
ldc c 70
out c
ldc c 105
out c
ldc c 114
out c
ldc c 115
out c
ldc c 116
out c
ldc c 32
out c
ldc c 105
out c
ldc c 110
out c
ldc c 116
out c
ldc c 101
out c
ldc c 103
out c
ldc c 101
out c
ldc c 114
out c
ldc c 58
out c
ldc c 32
out c
lda 0 8
in i
sto i
ldc i 16
sro i 0
ldc c 83
out c
ldc c 101
out c
ldc c 99
out c
ldc c 111
out c
ldc c 110
out c
ldc c 100
out c
ldc c 32
out c
ldc c 105
out c
ldc c 110
out c
ldc c 116
out c
ldc c 101
out c
ldc c 103
out c
ldc c 101
out c
ldc c 114
out c
ldc c 58
out c
ldc c 32
out c
lda 0 9
in i
sto i
ldc i 17
sro i 0
mst 1
lod i 0 8
lod i 0 9
cup 2 compareIntegersFunc
ujp main3
main2:
main3:
lod c 0 5
ldc c 'f'
equ c
fjp main4
ldc r 0.0
str r 0 10
ldc r 0.0
str r 0 11
ldc c 70
out c
ldc c 105
out c
ldc c 114
out c
ldc c 115
out c
ldc c 116
out c
ldc c 32
out c
ldc c 102
out c
ldc c 108
out c
ldc c 111
out c
ldc c 97
out c
ldc c 116
out c
ldc c 58
out c
ldc c 32
out c
lda 0 10
in r
sto r
ldc i 14
sro i 0
ldc c 83
out c
ldc c 101
out c
ldc c 99
out c
ldc c 111
out c
ldc c 110
out c
ldc c 100
out c
ldc c 32
out c
ldc c 102
out c
ldc c 108
out c
ldc c 111
out c
ldc c 97
out c
ldc c 116
out c
ldc c 58
out c
ldc c 32
out c
lda 0 11
in r
sto r
ldc i 15
sro i 0
mst 1
lod r 0 10
lod r 0 11
cup 2 compareFloatsFunc
ujp main5
main4:
main5:
retp
