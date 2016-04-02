import math

data = [{
    'time': '2012.12.10 21:10:30',
    'name': ['CSXY', 'FTD', 'GGGG', 'GYS', 'NYF', 'ROY', 'SYT', 'ZPZ'],
    'mpi': [35, 74, 120, 93, 260, 299, 69, 70],
}, {
    'time': '2012.12.10 21:10:48',
    'name': ['5', 'FTD', 'HIETA', 'KUMA', 'NIR', 'OOXXINC', 'OVERLOAD', 'TRISOMY'],
    'mpi': [213, 178, 399, 192, 83, 278, 95, 240],
}, {
    'time': '2012.12.10 21:10:59',
    'name': ['FTD', 'HEHE', 'HIETA', 'KIRITO', 'MTH', 'TAMELESS', 'TOM', 'WXY'],
    'mpi': [70, 107, 72, 99, 99, 69, 54, 98],
}, {
    'time': '2012.12.10 21:11:09',
    'name': ['FBY', 'FUCK', 'HHHHHH', 'KIRITO', 'OWO', 'RABBIT', 'TC', 'YAOBAIJU'],
    'mpi': [416, 220, 287, 286, 282, -27, 253, 131],
}, {
    'time': '2012.12.10 21:11:22',
    'name': ['CUPPY', 'EMINENCE', 'FLY', 'KIRITO', 'LILI', 'OOXXINC', 'OVERLOAD', 'TO'],
    'mpi': [111, 201, 219, 101, 199, 251, 94, 89],
}, {
    'time': '2012.12.10 21:11:38',
    'name': ['EXIBAR', 'FBY', 'HEHE', 'KHAOS', 'LOUIS', 'OOXXINC', 'TIGER', 'XWJ'],
    'mpi': [350, 432, 383, 394, 402, 399, 428, 279],
}, {
    'time': '2012.12.10 21:11:49',
    'name': ['CUPPY', 'IE', 'LILI', 'OOXXINC', 'OWO', 'PLAYER', 'ROY', 'TO'],
    'mpi': [307, 236, 264, 394, 294, 265, 320, 249],
}, {
    'time': '2012.12.10 21:11:58',
    'name': ['CM', 'FBY', 'NOVA', 'OOXXINC', 'OWO', 'SKYFALL', 'SOS', 'ZYB'],
    'mpi': [123, 157, 97, 151, 139, 152, 130, 135],
}, {
    'time': '2012.12.10 21:12:09',
    'name': ['ARA', 'FLY', 'HEHE', 'IRIDESCE', 'OOXXINC', 'SCARLETT', 'SOS', 'XAS'],
    'mpi': [278, 185, 267, 458, 415, 433, 331, 377],
}, {
    'time': '2012.12.10 21:12:38',
    'name': ['FLY', 'KIPO', 'KNIGHT', 'LILI', 'SOS', 'TIGER', 'XWJ', 'OOXXINC'],
    'mpi': [414, 393, 347, 339, 385, 393, 450, 391],
}, {
    'time': '2012.12.10 21:13:03',
    'name': ['KNIGHT', 'LILI', 'OOXXINC', 'PASKIN', 'XAS', 'XWJ', 'XXOO1NG', 'YCH'],
    'mpi': [397, 316, 390, 222, 352, 233, -35, 84],
}, {
    'time': '2012.12.10 21:13:15',
    'name': ['FBY', 'KNIGHT', 'LL', 'MLGB', 'NONO', 'SCARLETT', 'SOS', 'XAS'],
    'mpi': [329, 310, 232, 236, 296, 313, 272, 301],
}, {
    'time': '2012.12.10 21:13:27',
    'name': ['CSXY', 'CTP', 'FBY', 'MLGB', 'ROY', 'SCARLETT', 'XAS', 'OOXXINC'],
    'mpi': [252, 223, 296, 177, 151, 263, 257, 332],
}, {
    'time': '2012.12.10 21:13:37',
    'name': ['ALPHEN', 'EMANUEL', 'FBY', 'HEHE', 'LILI', 'MAJOR', 'MTH', 'OWO'],
    'mpi': [285, 396, 455, 416, 443, 399, 448, 413],
}, {
    'time': '2012.12.10 21:13:51',
    'name': ['CALIBURN', 'EXCALIBU', 'FBY', 'HEHE', 'MAJOR', 'ROY', 'ZJL', 'ZTQ'],
    'mpi': [272, 228, 298, 264, 221, 271, 152, 290],
}, {
    'time': '2012.12.10 21:14:09',
    'name': ['123456', 'CUPPY', 'HEHE', 'ICYXIAO', 'OOXXINC', 'OWO', 'SYT', 'XAS'],
    'mpi': [390, 371, 496, 494, 516, 446, 419, 423],
}, {
    'time': '2012.12.10 21:14:30',
    'name': ['APPLE', 'HEHE', 'FBY', 'STEVE', 'SCARLETT', 'CHERRY', 'YY', 'LALALA'],
    'mpi': [184, 367, 266, 276, 320, 293, 266, 224],
}, {
    'time': '2012.12.10 21:14:44',
    'name': ['KAT', 'YMCA', 'ZYB', 'MTH', 'KAT', 'TC', 'ROY', 'LEMON'],
    'mpi': [343, 447, 392, 426, 392, 300, 377, 329],
}, {
    'time': '2012.12.10 21:14:59',
    'name': ['OOXXINC', 'LILI', 'ROY', 'TIGER', 'IE', 'ZJL', 'LEMON', 'QS'],
    'mpi': [399, 424, 280, 391, 303, 275, 153, 387],
}, {
    'time': '2012.12.10 21:15:15',
    'name': ['FBY', 'LEXUSZON', 'OWO', 'TIGER', 'LEMON', 'JIMMY', 'OOXXINC', 'BABEL'],
    'mpi': [308, 235, 332, 346, 221, 275, 344, 283],
}, {
    'time': '2012.12.10 21:15:30',
    'name': ['BABYLONI', 'JIMMY', 'LILI', 'LITTLE', 'MYSLY', 'ROY', 'SYT', 'XAS'],
    'mpi': [308, 222, 285, 266, 228, 252, 319, 282],
}, {
    'time': '2012.12.10 21:15:44',
    'name': ['BABYLONI', 'HEHE', 'ICYXIAO', 'JIMMY', 'OOXXINC', 'OWO', 'PEIPEI', 'SYT'],
    'mpi': [515, 435, 480, 403, 608, 510, 189, 478],
}, {
    'time': '2012.12.10 21:15:56',
    'name': ['AILE', 'CHROME', 'FSC', 'IE', 'NEO', 'OOXXINC', 'OWO', 'ZZ95'],
    'mpi': [89, 159, 268, 279, 309, 342, 311, 162],
}, {
    'time': '2012.12.10 21:16:07',
    'name': ['ABSTERGO', 'COOPER', 'HEHE', 'OOXXINC', 'OWO', 'ROY', 'TRISOMY', 'ZTQ'],
    'mpi': [165, 258, 184, 256, 186, 308, 105, 252],
}, {
    'time': '2012.12.10 21:16:17',
    'name': ['COOPER', 'MTH', 'NEO', 'ROY', 'TRISOMY', 'XAS', 'ZJL', 'ZYB'],
    'mpi': [84, 110, 124, 89, 88, 119, 62, 101],
}, {
    'time': '2012.12.10 21:21:57',
    'name': ['KHAOS', 'ROY', 'FBY', 'CTP', 'NIRVANAC', 'ABSTERGO', 'ZTQ', 'SYT'],
    'mpi': [374, 264, 354, 185, 261, 279, 374, 358],
}, {
    'time': '2012.12.10 21:22:23',
    'name': ['XAS', 'XWJZSGD', 'FLY', 'ROY', 'KHAOS', 'OWO', 'JERRY', 'LILI'],
    'mpi': [518, 312, 472, 427, 381, 469, 506, 462],
}, {
    'time': '2012.12.10 21:22:34',
    'name': ['EXIBAR', 'KHAOS', 'LILI', 'OOXXINC', 'ROY', 'TCL', 'ZZWDHS'],
    'mpi': [325, 443, 410, 439, 437, 330, 317],
}, {
    'time': '2012.12.10 21:22:45',
    'name': ['OOXXINC', 'ICYXIAO', 'ZTQ', 'FLY', 'LILI', 'ZZ95', 'JIECAO'],
    'mpi': [417, 367, 378, 395, 295, 363, 386],
}, {
    'time': '2012.12.10 21:22:56',
    'name': ['AOA', 'ASDMINRE', 'BILIBILI', 'EXIBAR', 'FLY', 'OOXXINC', 'OVERLOAD', 'QS'],
    'mpi': [210, 208, 245, 105, 165, 316, 205, 285],
}, {
    'time': '2012.12.10 21:23:06',
    'name': ['FLY', 'HIGH', 'IE', 'OOXXINC', 'OVERLOAD', 'PHANTOM', 'TIGER', 'XAS'],
    'mpi': [406, 172, 211, 110, 311, 284, 275, 309],
}, {
    'time': '2012.12.10 21:23:18',
    'name': ['CM', 'EXIBAR', 'FBY', 'FLY', 'OOXXINC', 'LILI', 'OWO', 'QS'],
    'mpi': [204, 331, 532, 568, 112, 82, 315, 327],
}, {
    'time': '2012.12.10 21:23:28',
    'name': ['DANTE', 'EXIBAR', 'KAT', 'KEVIN', 'LILI', 'NIWEI', 'ZQM', 'TC'],
    'mpi': [224, 230, 357, 456, 476, 191, 256, 279],
}, {
    'time': '2012.12.10 21:23:40',
    'name': ['BIENUEWO', 'EXIBAR', 'FLY', 'OOXXINC', 'JOK', 'LILI', 'MESEYOUG', 'MYSLY'],
    'mpi': [164, 159, 240, 250, 266, 333, 222, 113],
}, {
    'time': '2012.12.10 21:23:50',
    'name': ['KAT', 'KAT', 'TC', 'OVERLOAD', 'LC', 'IE'],
    'mpi': [518, 344, 303, 351, 213, 114],
}, {
    'time': '2012.12.10 21:24:01',
    'name': ['AIR', 'ARA', 'FLY', 'OOXXINC', 'HHHHHH', 'SAS', 'ICYXIAO', 'ZTQ'],
    'mpi': [596, 440, 649, 512, 585, 542, 598, 665],
}, {
    'time': '2012.12.10 21:24:11',
    'name': ['EVEN', 'EXIBAR', 'FLY', 'OOXXINC', 'HHHHHH', 'OWO', 'STEVENJI', 'ICYXIAO'],
    'mpi': [134, 242, 170, 233, 158, 165, 243, 208],
}, {
    'time': '2012.12.10 21:24:22',
    'name': ['LUCH', 'AIR', 'XAS', 'TC', 'OOXXINC', 'AWK', 'NW', 'HHHHHH'],
    'mpi': [204, 319, 176, 176, 255, 281, 180, 486],
}, {
    'time': '2012.12.10 21:24:34',
    'name': ['OOXXINC', 'XAS', 'FLY', 'LUCH', 'JERRY'],
    'mpi': [348, 241, 233, 235, 225],
}, {
    'time': '2012.12.10 21:24:43',
    'name': ['OOXXINC', 'ICYXIAO', 'OWO', 'XAS', 'FLY', 'FSC', 'CHESTER', 'IE'],
    'mpi': [563, 544, 401, 480, 554, 351, 353, 559],
}, {
    'time': '2012.12.10 21:24:54',
    'name': ['JIMMY', 'RA', 'XAS', 'YY', 'COOPER', 'OOXXINC', 'FLY', 'FSC'],
    'mpi': [176, 214, 275, 159, 186, 256, 95, 215],
}, {
    'time': '2012.12.10 21:25:33',
    'name': ['YY', 'DK', 'RA', 'LEAF', 'OWO', 'SKY', 'ZZ95', 'OOXXINC'],
    'mpi': [130, 34, 259, 145, 198, 136, 94, 38],
}, {
    'time': '2012.12.10 21:25:43',
    'name': ['OOXXINC', 'KAT', 'JLEE', 'IE', 'FLY', 'SOLEILL', 'HAHA', 'IVYSUI'],
    'mpi': [698, 635, 585, 707, 746, 580, 530, 760],
}, {
    'time': '2012.12.10 21:25:57',
    'name': ['NIR', 'OOXXINC', 'CHUNGE', 'MJ', 'HIGH', '0000', 'BIRD', 'LEMON'],
    'mpi': [488, 477, 524, 371, 495, 503, 425, 449],
}, {
    'time': '2012.12.10 21:42:49',
    'name': ['OOXXINC', 'TC', 'NW', 'JZW', 'TZP', 'BX', 'LX', 'XC'],
    'mpi': [344, 365, 263, 301, 282, 291, 275, 16],
}, {
    'time': '2012.12.10 21:43:04',
    'name': ['LEAF', 'JLEE', 'SKY', 'BIRD', 'KAT', 'VIGHTT', 'CM', 'EREDNUST'],
    'mpi': [577, 472, 614, 417, 475, 421, 484, 467],
}, {
    'time': '2012.12.10 21:43:20',
    'name': ['EAGER', 'LEAF', 'SKY', 'YUU', 'KEV', 'CM', 'SA', 'FY'],
    'mpi': [294, 325, 407, 393, 346, 541, 466, 447],
}, {
    'time': '2012.12.10 21:43:30',
    'name': ['XIAO6', 'CAOCAO', 'OOXXINC', 'KAT', 'EAGER', 'V', 'CHONG', 'ALLEZ'],
    'mpi': [365, 340, 390, 307, 358, 328, 361, 431],
}, {
    'time': '2012.12.10 21:43:43',
    'name': ['XIAO6', 'MAJOR', 'SKY', 'OOXXINC', 'CHONG', 'FLY', 'TIGER', 'ALLEZ'],
    'mpi': [280, 296, 271, 331, 270, 298, 293, 326],
}, {
    'time': '2012.12.10 21:43:55',
    'name': ['HENI', 'TIGER', 'UD', 'BUXIN', 'TC', 'YULUO', 'SKY', 'XD'],
    'mpi': [416, 442, 414, 467, 401, 397, 406, 423],
}, {
    'time': '2012.12.10 21:44:06',
    'name': ['AF', 'SKY', 'ENEN', 'TVT', 'KAT', 'LEAF', 'BIRD', 'ANTONIO'],
    'mpi': [266, 408, 292, 333, 352, 458, 304, 411],
}, {
    'time': '2012.12.10 21:44:18',
    'name': ['S1', 'S2', 'KEV', 'GDU', 'LEAF', 'LEAF', 'LIPTONER', 'SKY'],
    'mpi': [503, 377, 456, 413, 447, 459, 496, 408],
}, {
    'time': '2012.12.10 21:59:12',
    'name': ['FLY', 'APPLE', 'EAGER', 'O', 'CHERRY', 'KAT', 'FUCK', 'OOXXINC'],
    'mpi': [359, 480, 424, 439, 340, 458, 377, 484],
}, {
    'time': '2012.12.10 21:44:53',
    'name': ['ARA', 'OOXXINC', 'KAT', 'TC', 'JZW', 'DHH', 'TIGER', 'ALLEZ'],
    'mpi': [269, 333, 300, 281, 241, 281, 354, 356],
}, {
    'time': '2012.12.10 21:45:02',
    'name': ['GE', 'TIGER', 'ARA', 'MAJOR', 'ALLEZ', 'OBSERVER', 'OOXXING', 'YY'],
    'mpi': [416, 581, 448, 473, 457, 404, 394, 557],
}, {
    'time': '2012.12.10 21:45:12',
    'name': ['TIGER', 'HIGH', 'ARA', 'ALLEZ', 'OOXXINC', 'XIAO6', 'LUOLUO', 'LEE'],
    'mpi': [347, 301, 263, 346, 292, 206, 303, 315],
}, {
    'time': '2012.12.10 21:45:23',
    'name': ['TIGER', 'LUOLUO', 'KOBE', 'LAOLIU', 'ZHC', 'DAXIONG', 'OOXXINC', 'XIAO6'],
    'mpi': [463, 469, 427, 463, 340, 520, 489, 498],
}, {
    'time': '2012.12.10 21:45:37',
    'name': ['PAUL', 'HIGH', 'XIAO6', 'TIGER', 'OOXXINC', 'FY', 'FLY', 'LJY'],
    'mpi': [414, 317, 377, 549, 395, 337, 455, 282],
}, {
    'time': '2012.12.10 21:45:58',
    'name': ['BUXIN', 'TC', 'SKY', 'OOXXINC', 'KEVIN', 'LCJ', 'YUU', 'XIAO6'],
    'mpi': [420, 460, 416, 497, 526, 181, 446, 464],
}, {
    'time': '2012.12.10 21:46:09',
    'name': ['TC', 'EAGER', 'SKY', 'CAONIAO', 'KEA', 'APPLE', 'OOXXINC', 'ADA'],
    'mpi': [457, 296, 382, 397, 526, 457, 451, 357],
}, {
    'time': '2012.12.10 21:46:20',
    'name': ['JLEE', 'SKY', 'VIGHTT', 'KOJ', 'LSY', 'LEAF', 'PAUL', 'TIGER'],
    'mpi': [380, 508, 383, 527, 425, 432, 382, 414],
}, {
    'time': '2012.12.10 21:46:29',
    'name': ['EAGER', 'KAT', 'APPLE', 'SKY', 'LEAF', 'CHONG', 'BIRD', 'OOXXINC'],
    'mpi': [273, 364, 296, 262, 403, 315, 221, 366],
}, {
    'time': '2012.12.10 21:56:08',
    'name': ['HF', 'OWO', 'LILI', 'ZZ95', 'KHAOS', 'RHAPSODY', 'ROY', 'XAS'],
    'mpi': [325, 284, 322, 227, 322, 288, 271, 273],
}, {
    'time': '2012.12.10 21:56:21',
    'name': ['XAS', 'EXIBAR', 'OWO', 'KYW', 'OOXXINC', 'NIRVANAC', 'LIEBESLE', 'CAMARADE'],
    'mpi': [482, 413, 472, 342, 443, 453, 490, 494],
}, {
    'time': '2012.12.10 21:56:57',
    'name': ['AVI', 'BUHUIWAN', 'EVEN', 'EXIBAR', 'FLY', 'LILI', 'OWO', 'ZI'],
    'mpi': [371, -44, 424, 432, 742, 372, 465, 443],
}, {
    'time': '2012.12.10 21:57:09',
    'name': ['EVEN', 'EXIBAR', 'FLY', 'OOXXINC', 'LILI', 'MYSLY', 'OWO', 'AVI'],
    'mpi': [348, 396, 320, 440, 383, 402, 423, 333],
}, {
    'time': '2012.12.10 21:57:24',
    'name': ['XAS', 'ZTQ', 'OWO', 'GMAIL', 'FSC', 'KHAOS', 'TIGER', 'SOLEILL'],
    'mpi': [393, 462, 493, 332, 425, 533, 554, 369],
}, {
    'time': '2012.12.10 21:57:33',
    'name': ['FSC', 'KAT', 'SPY', 'KHAOS', 'OWO', 'YY', 'MYSLY', 'EXIBAR'],
    'mpi': [398, 539, 623, 645, 579, 657, 565, 708],
}, {
    'time': '2012.12.10 21:57:43',
    'name': ['OWO', 'KHAOS', 'FSC', 'ZTQ', 'LEMON', 'AAA', 'HIGH', 'FLY'],
    'mpi': [311, 504, 417, 522, 435, 427, 380, 380],
}, {
    'time': '2012.12.10 21:57:56',
    'name': ['SOLEILL', 'JLEE', 'NI', 'OWO', 'RA', 'ICYXIAO', 'ZZ95', 'EXIBAR'],
    'mpi': [434, 183, 170, 399, 350, 214, 269, 244],
}, {
    'time': '2012.12.10 21:58:11',
    'name': ['QS', 'RA', 'MYSLY', 'SYT', 'OWO', 'ZTQ', 'JIMMY', 'JERRY'],
    'mpi': [401, 372, 246, 398, 374, 394, 430, 427],
}, {
    'time': '2012.12.10 21:58:22',
    'name': ['KHAOS', 'MYSLY', 'MEMORY', 'ZTQ', 'OWO', 'YY', 'XAS', 'IE'],
    'mpi': [468, 438, 441, 644, 574, 660, 660, 518],
}, {
    'time': '2012.12.10 21:58:35',
    'name': ['KHAOS', 'OWO', 'XAS', 'RA', 'IE', 'ARA', 'JIMMY', 'OOXXINC'],
    'mpi': [496, 407, 415, 430, 448, 532, 506, 512],
}, {
    'time': '2012.12.10 21:59:37',
    'name': ['KHAOS', 'ICYXIAO', 'RA', 'OWO', 'CM', 'WSY', 'ARA', 'AB'],
    'mpi': [533, 523, 469, 464, 523, 500, 508, 382],
}, {
    'time': '2012.12.10 21:59:00',
    'name': ['IVYSUI', 'SOLEILL', 'EXIBAR', 'ICYXIAO', 'DZMM', 'YY', 'ARA', 'AIR'],
    'mpi': [378, 270, 337, 339, 435, 365, 397, 417],
}, {
    'time': '2012.12.10 21:59:24',
    'name': ['SJ', 'CM', 'IE', 'ARA', 'ZTP', 'XIAO6', 'ARES', 'IVYSUI'],
    'mpi': [526, 496, 348, 498, 435, 517, 466, 398],
}, {
    'time': '2012.12.14 20:53:58',
    'name': ['ARZUS', 'CUPPY', 'FUCK', 'HEHE', 'LIVPOOL', 'MTH', 'OOXXINC', 'ROY'],
    'mpi': [289, 378, 252, 361, 303, 337, 406, 323],
}, {
    'time': '2012.12.14 21:46:42',
    'name': ['CUPPY', 'HEHE', 'LILI', 'LIVPOOL', 'MTH', 'OOXXINC', 'QUQUQUQ', 'ROY'],
    'mpi': [219, 186, 173, 168, 204, 196, 237, 164],
}, {
    'time': '2012.12.15 18:55:02',
    'name': ['ARA', 'FBY', 'FTD', 'HIETA', 'LYF', 'OOXXINC', 'ROY', 'SSM'],
    'mpi': [318, 318, 273, 348, 262, 370, 268, 280],
}, {
    'time': '2012.12.15 19:29:04',
    'name': ['ARA', 'FBY', 'FTD', 'HIETA', 'LILI', 'ROY', 'SSM', 'ZJK'],
    'mpi': [300, 294, 251, 269, 285, 226, 176, 252],
}, {
    'time': '2012.12.15 20:38:35',
    'name': ['FTD', 'KIRITO', 'LILI', 'LYF', 'NOVA', 'OOXXINC', 'SSM', 'ZJK'],
    'mpi': [314, 370, 358, 349, 334, 366, 321, 349],
}, {
    'time': '2012.12.17 22:59:35',
    'name': ['EXIBAR', 'FLY', 'FTD', 'KHIGHT', 'FIKRI', 'SSM', 'XAS', 'XWJ'],
    'mpi': [258, 241, 279, 317, 114, 275, 250, 157],
}, {
    'time': '2012.12.21 22:16:47',
    'name': ['AYA', 'CUPPY', 'OOXXINC', 'FTD', 'GFADGFDS', 'KIRITO', 'LYF', 'WXY'],
    'mpi': [237, 270, 320, 225, 254, 170, 245, 302],
}, {
    'time': '2012.12.22 20:51:02',
    'name': ['CUPPY', 'ALIVE', 'FTD', 'HEHE', 'KIRITO', 'LILI', 'LJQ', 'XAS'],
    'mpi': [184, 218, 237, 129, 169, 252, -7, 165],
}, {
    'time': '2012.12.22 22:22:41',
    'name': ['ALIVE', 'AYA', 'CUPPY', 'EMINENCE', 'FTD', 'GODLIKE', 'HEHE', 'KIRITO'],
    'mpi': [161, 250, 287, 282, 200, 273, 213, 308],
}, {
    'time': '2012.12.23 20:51:40',
    'name': ['ALIVE', 'FTD', 'GODLIKE', 'KHAOS', 'KIRITO', 'LILI', 'MARS', 'TIGER'],
    'mpi': [235, 120, 243, 209, 250, 179, 217, 288],
}, {
    'time': '2012.12.31 19:44:34',
    'name': ['LILI', 'FLY', 'COOPER', 'MARS', 'DS', 'KIRITO', 'WXY', 'SCARLETT'],
    'mpi': [404, 379, 364, 402, 409, 387, 386, 369],
}, {
    'time': '2012.12.31 19:44:58',
    'name': ['LCT', 'ROY', 'WXY', 'LILI', 'KIRITO', 'ALIVE', 'HEHE', 'XAS'],
    'mpi': [140, 240, 292, 333, 274, 271, 279, 311],
}, {
    'time': '2012.12.31 20:53:38',
    'name': ['CUPPY', 'JLEE', 'KIRITO', 'LIVPOOL', 'LOG24', 'OOXXINC', 'ROY', 'WXY'],
    'mpi': [122, 39, 126, 106, -2, 174, 68, 16],
}, {
    'time': '2012.12.31 22:16:18',
    'name': ['CUPPY', 'FTD', 'GODLIKE', 'HEHE', 'JL2B', 'JLEE', 'OWO', 'ZZLY'],
    'mpi': [373, 355, 357, 174, 216, 239, 310, 231],
}, {
    'time': '2013.1.5 19:57:32',
    'name': ['A', 'FTD', 'GODLIKE', 'KIRITO', 'OOXXINC', 'OVO', 'TIGER', 'UNRULY'],
    'mpi': [144, 358, 264, 266, 281, 245, 244, 249],
}, {
    'time': '2013.1.5 19:57:51',
    'name': ['KUMA', 'KIRITO', 'TC', 'LCT', 'MARS', 'CUPPY', 'EXIBAR', 'FLY'],
    'mpi': [103, 240, 154, 232, 245, 241, 102, 146],
}, {
    'time': '2013.1.6 20:55:55',
    'name': ['CUPPY', 'FTD', 'KIRITO', 'MARS', 'OOXXINC', 'UNRULY', 'WHCXE', 'ZEUS'],
    'mpi': [322, 285, 314, 292, 298, 214, 79, 301],
}, {
    'time': '2013.1.18 19:51:53',
    'name': ['AWAY', 'FTD', 'HEHE', 'KIRITO', 'LILI', 'OOXXINC', 'ROY', 'TIGER'],
    'mpi': [451, 339, 420, 382, 412, 408, 353, 427],
}, {
    'time': '2013.1.18 21:06:08',
    'name': ['CAT', 'CUPPY', 'FTD', 'HEHE', 'LILI', 'MARX', 'MM', 'OOXXINC'],
    'mpi': [153, 204, 193, 176, 212, 224, 214, 208],
}, {
    'time': '2013.1.18 22:04:19',
    'name': ['CAT', 'EMINENCE', 'I8', 'KIRITO', 'LILI', 'MM', 'OOXXINC', 'TB'],
    'mpi': [73, 162, 112, 57, 162, 106, 258, 272],
}, {
    'time': '2013.1.25 20:03:27',
    'name': ['EMINENCE', 'FTD', 'HM', 'INSPRATI', 'KHAOS', 'KIRITO', 'LCG', 'OOXXINC'],
    'mpi': [265, 300, 300, 186, 315, 310, 282, 332],
}, {
    'time': '2013.1.25 21:10:35',
    'name': ['EMINENCE', 'FTD', 'INSPRATI', 'KIRITO', 'LCG', 'LILI', 'OOXXINC', 'RAB'],
    'mpi': [219, 299, 117, 177, 186, 248, 281, 168],
}, {
    'time': '2013.1.26 21:17:25',
    'name': ['AYA', 'EMINENCE', 'FTD', 'HHM', 'INSPRATI', 'KAT', 'OOXXINC', 'TIGER'],
    'mpi': [277, 268, 187, 249, 148, 359, 239, 223],
}, {
    'time': '2013.1.27 20:12:54',
    'name': ['CAT', 'FLY', 'FTD', 'HM', 'INSPRATI', 'LCT', 'MIANMIAN', 'OOXXINC'],
    'mpi': [243, 293, 249, 288, 170, 271, 135, 302],
}, {
    'time': '2013.1.27 21:44:49',
    'name': ['CAT', 'INSPRATI', 'LILI', 'MATT', 'OOXXINC', 'OWO', 'RABBIT', 'WXY'],
    'mpi': [163, 142, 211, 161, 208, 193, 191, 183],
}, {
    'time': '2013.1.31 22:25:37',
    'name': ['KIRITO', 'MATT', 'LILI', 'FTD', 'ASH', 'INSPRATI', 'OOXXINC', 'OWO'],
    'mpi': [245, 239, 345, 272, 281, 179, 244, 231],
}, {
    'time': '2013.2.2 19:10:50',
    'name': ['MATT', 'XWJ', 'KIRITO', 'TC', 'FLY', 'INSPRATI', 'MYSLY', 'FTD'],
    'mpi': [94, 80, 210, 130, 282, 114, -62, 122],
}, {
    'time': '2013.2.2 19:58:20',
    'name': ['OOXXINC', 'KIRITO', 'LILI', 'INSPRATI', 'EMINENCE', 'TIGER', 'MYSLY', 'MATT'],
    'mpi': [497, 489, 427, 311, 411, 409, 346, 318],
}, {
    'time': '2013.2.3 17:21:02',
    'name': ['L', 'LILI', 'MATT', 'FTD', 'XAS', 'FLY', 'MYSLY', 'OOXXINC'],
    'mpi': [315, 225, 148, 183, 271, 101, 172, 265],
}, {
    'time': '2013.2.3 18:19:21',
    'name': ['EMINENCE', 'MATT', 'MYSLY', 'FLY', 'LILI', 'WXY', 'WWW', 'OOXXINC'],
    'mpi': [269, 273, 246, 260, 257, 287, 251, 376],
}, {
    'time': '2013.2.3 20:29:20',
    'name': ['CYNTHIA', 'INSPRATI', 'WXY', 'SOMNUSM', 'FTD', 'TIGER', 'JIANGYOU', 'CUPPY'],
    'mpi': [155, 138, 131, 214, 228, 263, 111, 107],
}, {
    'time': '2013.2.3 22:10:26',
    'name': ['INSPRATI', 'MATT', 'UNRULY', 'SOMNUSM', '5238', 'MOMO', 'TIGER', 'KIRITO'],
    'mpi': [225, 172, 197, 318, 188, 128, 180, 262],
}, {
    'time': '2013.2.4 20:05:55',
    'name': ['LILI', 'PASTUREK', 'GODLIKE', 'INSPRATI', 'LOISE', 'YL', 'KIRITO', 'DAY'],
    'mpi': [370, 267, 317, 263, 265, 241, 291, 198],
}, {
    'time': '2013.2.4 20:06:13',
    'name': ['CADAE', 'FTD', 'FTD', 'INSPRATI', 'KIRITO', 'LILI', 'MATT', 'QQQ'],
    'mpi': [93, 242, 277, 183, 352, 381, 233, 158],
}, {
    'time': '2013.2.4 21:12:58',
    'name': ['MATT', 'INSPRATI', 'WESIQ', 'MEREDITH', 'CUPPY', 'TSJ', 'WH', 'KIRITO'],
    'mpi': [187, 174, 373, 248, 226, 181, 88, 308],
}, {
    'time': '2013.2.5 20:29:54',
    'name': ['GODLIKE', 'FTD', 'LILI', 'TIGER', 'WYC', 'MATT', 'BHY', 'OOXXINC'],
    'mpi': [341, 295, 185, 317, 142, 216, 256, 291],
}, {
    'time': '2013.2.5 23:25:09',
    'name': ['KIRITO', 'KHAOS', 'GODLIKE', 'WYC', 'LILI', 'TSJ', 'INSPRATI', 'FTD'],
    'mpi': [277, 352, 376, 178, 334, 251, 208, 293],
}, {
    'time': '2013.2.5 23:25:30',
    'name': ['WYC', 'KHAOS', 'EMINENCE', 'INSPRATI', 'KIRITO', 'FTD', 'LILI', 'GODLIKE'],
    'mpi': [315, 508, 548, 406, 576, 308, 501, 639],
}, {
    'time': '2013.2.6 17:03:43',
    'name': ['GODLIKE', 'KIRITO', 'TONY', 'INSPRATI', 'OOXXINC', 'FTD', '111', 'UNRULY'],
    'mpi': [432, 392, 263, 268, 382, 251, 399, 333],
}, {
    'time': '2013.2.8 16:52:42',
    'name': ['CANDY', 'INSPRATI', 'FTD', 'CUPPY', 'WYC', 'MATT', 'GODLIKE', 'CNMD'],
    'mpi': [175, 227, 380, 301, 165, 326, 373, 307],
}, {
    'time': '2013.2.8 16:53:02',
    'name': ['INSPRATI', 'GODLIKE', 'KIRITO', 'MARS', 'TSJ', 'FLY'],
    'mpi': [312, 375, 364, 413, 313, 393],
}, {
    'time': '2013.2.8 16:53:19',
    'name': ['INSPRATI', 'UNRULY', 'MATT', 'KIRITO', 'GODLIKE', '8', 'EXIBAR', 'FTD'],
    'mpi': [217, 102, 142, 405, 379, 377, 96, 94],
}, {
    'time': '2013.2.8 16:53:42',
    'name': ['CNMD', 'AVALON', 'MATT', 'HEHE', 'KIRITO', 'CANDY', 'WYC', 'CUPPY'],
    'mpi': [406, 437, 514, 201, 538, 433, 248, 470],
}, {
    'time': '2013.2.8 16:53:55',
    'name': ['MATT', 'KIRITO', 'GODLIKE', 'MAH', 'FTD', 'CUPPY', 'ADAI', 'CAICAIWO'],
    'mpi': [257, 280, 386, 354, 304, 337, 152, 335],
}, {
    'time': '2013.2.8 16:54:06',
    'name': ['00', 'EMINENCE', 'GODLIKE', 'FLY', 'SWEET', 'MATT', 'KIRITO', 'WYC'],
    'mpi': [383, 407, 416, 432, 376, 425, 420, 223],
}, {
    'time': '2013.2.8 16:54:16',
    'name': ['MATT', 'WYC', 'GODLIKE', 'FLY', 'CUPPY', 'KIRITO', 'CANDY', 'FTD'],
    'mpi': [434, 280, 564, 419, 479, 510, 487, 478],
}, {
    'time': '2013.2.8 17:03:54',
    'name': ['WYC', 'MATT', 'AVALON', 'EMINENCE', 'FTD', 'A', 'GODLIKE', 'KIRITO'],
    'mpi': [269, 610, 470, 502, 400, 402, 478, 546],
}, {
    'time': '2013.2.8 21:24:52',
    'name': ['MATT', 'AVALON', 'GODLIKE', 'LILI', 'CUPPY', '00', 'KIRITO', 'INSPRATI'],
    'mpi': [314, 298, 343, 312, 295, 317, 306, 304],
}, {
    'time': '2013.2.8 21:25:08',
    'name': ['GODLIKE', 'KIRITO', 'MATT', 'LILI', 'CUPPY', 'INSPRATI', 'THEEND', 'FTD'],
    'mpi': [97, 86, 33, 325, 83, 291, -61, 119],
}, {
    'time': '2013.2.9 18:16:25',
    'name': ['INSPRATI', 'WYC', 'MATT', 'WH', 'MPI', 'HOUHOU', 'CNMD', 'EMINENCE'],
    'mpi': [286, 168, 320, 152, 266, 308, 233, 282],
}, {
    'time': '2013.2.9 22:55:54',
    'name': ['KIRITO', 'SWEET', 'MATT', 'INSPRATI', 'OSO', 'MARS', 'GODLIKE', 'SPARK'],
    'mpi': [67, 110, 192, 57, 12, 44, 214, 84],
}, {
    'time': '2013.2.10 0:28:08',
    'name': ['PASTUREK', 'INSPRATI', 'FLY', 'WH', 'HEHE', 'OOXXINC', 'MAHAN', 'EMINENCE'],
    'mpi': [412, 476, 411, 95, 483, 436, 507, 494],
}, {
    'time': '2013.2.10 15:38:23',
    'name': ['GODLIKE', 'INSPRATI', 'MATT', 'OOXXINC', 'FLY', 'FTD', 'KIRITO', 'HEHE'],
    'mpi': [584, 441, 576, 605, 591, 600, 603, 493],
}, {
    'time': '2013.2.10 15:41:24',
    'name': ['MATT', 'INSPRATI', 'DK', 'RP', 'WYC', 'WH'],
    'mpi': [370, 317, 231, 303, 336, 276],
}, {
    'time': '2013.2.12 20:02:23',
    'name': ['D', 'GODLIKE', 'MATT', 'INSPRATI', 'SPARK', 'FTD', 'KIRITO'],
    'mpi': [11, 282, 125, -2, 67, 23, -3],
}, {
    'time': '2013.2.12 20:02:39',
    'name': ['INSPRATI', 'ANGELINA', 'WYC', 'KAT', 'SPARK', 'MATT', 'FTD', 'OOXXAI'],
    'mpi': [321, 273, 217, 453, 450, 515, 431, 385],
}, {
    'time': '2013.2.12 21:37:39',
    'name': ['TIGER', 'GODLIKE', 'MATT', 'FLY', 'INSPRATI', 'KIRITO', 'WYC', 'OOXXINC'],
    'mpi': [199, 329, 330, 316, 162, 195, 216, 213],
}, {
    'time': '2013.2.13 19:59:11',
    'name': ['WYC', 'INSPRATI', 'GODLIKE', 'LILI', 'LIZZY', 'SPARK', 'ARZUS', 'ACU'],
    'mpi': [207, 304, 300, 338, 314, 276, 230, 311],
}, {
    'time': '2013.2.13 21:22:47',
    'name': ['MATT', 'KIRITO', 'INSPRATI', 'WYC', 'CSXY', 'IVYSUI', 'LILI', 'AYA'],
    'mpi': [214, 304, 221, 241, 200, 291, 465, 233],
}, {
    'time': '2013.2.14 20:01:17',
    'name': ['214', 'DK', 'NOTHING', 'WYCSLY', 'INSPRATI', 'MATT', 'FLY', 'KIRITO'],
    'mpi': [229, 111, 188, 70, 170, 113, 248, 246],
}, {
    'time': '2013.2.15 11:22:14',
    'name': ['INSPRATI', 'GODLIKE', 'MATT', 'TIGER', 'NOTHING', 'AI1', 'AI2', 'AI3'],
    'mpi': [67, 407, 370, 183, 71, 146, 156, 144],
}, {
    'time': '2013.2.15 11:22:34',
    'name': ['GODLIKE', 'MATT', 'NOTHING', 'I8', 'INSOMNIA', 'WYC', 'LILI', 'TC'],
    'mpi': [370, 387, 334, 381, 414, 231, 411, 340],
}, {
    'time': '2013.2.15 23:04:06',
    'name': ['INSPRATI', 'JIECAO', 'FLY', 'KIRITO', 'OOXXINC', 'COMP1', 'COMP2', 'COMP3'],
    'mpi': [309, 359, 317, 337, 305, 306, 306, 306],
}, {
    'time': '2013.2.20 20:31:30',
    'name': ['SPARK', 'GODLIKE', 'MATT', 'R', 'FTD', 'FTD', 'INSPRATI', 'KIRITO'],
    'mpi': [125, 212, 191, 204, 46, 66, 49, 119],
}, {
    'time': '2013.2.20 20:36:27',
    'name': ['1', 'WH', 'WYC', 'JIONG', 'MATT', 'GODLIKE', 'KIRITO', 'FTD'],
    'mpi': [207, 252, 7, 216, 311, 328, 204, 275],
}, {
    'time': '2013.2.20 20:37:00',
    'name': ['KIRITO', 'FTD', 'FTD', 'GODLIKE', 'MATT', 'WOLEGEQU', 'WH', 'SPARK'],
    'mpi': [272, 344, 255, 353, 298, 280, 268, 271],
}, {
    'time': '2013.2.25 18:19:53',
    'name': ['WOLEGEQU', 'L', 'GODLIKE', 'I', 'MATT', 'INSPRATI', 'FTD', 'FLY'],
    'mpi': [201, 305, 285, 327, 385, 172, 208, 290],
}, {
    'time': '2013.2.25 18:20:05',
    'name': ['INSPRATI', 'ANGELINA', 'CYNTHIA', 'WOLEGEQU', 'SPARK', 'MATT', 'FTD', 'GODGIFT'],
    'mpi': [356, 220, 206, 229, -11, 159, 193, 49],
}, {
    'time': '2013.2.25 18:20:26',
    'name': ['GODGIFT', 'INSPRATI', 'GODLIKE', 'KIRITO', 'ANGELINA', 'MATT', 'FTD', 'H'],
    'mpi': [435, -1, 498, 500, 236, 185, 211, 147],
}, {
    'time': '2013.2.25 18:20:38',
    'name': ['KIRITO', 'INSPRATI', 'GODLIKE', 'WOLEGEQU', 'MATT', 'ITSF8'],
    'mpi': [82, 208, 173, 215, 107, 261],
}, {
    'time': '2013.5.5 21:05:21',
    'name': ['YUYU', 'GODLIKE', 'FTD', 'ITSF8', 'MADLAB', 'INSPRATI', 'STYLE', 'OOXXINC'],
    'mpi': [304, 374, 328, 324, 292, 148, 235, 308],
}, {
    'time': '2013.5.5 21:09:16',
    'name': ['ZHY', 'ZHANGSHU', 'KIRITO', 'MATT', 'YUYU', 'CRAP', 'LOOK', 'LINDA'],
    'mpi': [261, 282, 286, 299, 225, 339, 198, 182],
}, {
    'time': '2013.5.5 21:10:56',
    'name': ['OOXXINC', 'MATT', 'GODLIKE', 'I8', 'LILI', 'INSPRATI'],
    'mpi': [436, 512, 463, 434, 382, 88],
}, {
    'time': '2013.5.5 21:11:40',
    'name': ['INSPRATI', 'I8', '1', 'OOXXINC', 'ANGELINA', 'GODLIKE'],
    'mpi': [219, 382, 407, 394, 248, 390],
}, {
    'time': '2013.5.5 21:12:30',
    'name': ['GODLIKE', 'MATT', 'WH', 'W8198H', 'FTD', 'LILI'],
    'mpi': [262, 261, 229, 292, 195, 299],
}, {
    'time': '2013.5.5 21:12:47',
    'name': ['LINDA', 'MATT', 'WH', 'KIRITO', 'ZHY', 'LOVEASN', 'FTD', 'ZHANGSHU'],
    'mpi': [158, 325, 214, 349, 169, 80, 223, 11],
}, {
    'time': '2013.5.5 21:13:43',
    'name': ['SIR', 'INSPRATI', 'ITSF8', 'MATT', 'YUYU', 'GODLIKE', 'AJ', 'JIMMY'],
    'mpi': [77, 199, 152, 130, 177, 256, 59, 76],
}, {
    'time': '2013.5.5 21:13:59',
    'name': ['GODLIKE', 'MATT', 'BINGJR', 'INSPRATI', '7LAN', 'LILI'],
    'mpi': [338, 455, 323, 236, 467, 270],
}, {
    'time': '2013.5.5 21:14:28',
    'name': ['KIRITO', 'STYLE', 'ZAP', 'AJ', 'FTD', 'MATT', 'JIMMY', 'LYT'],
    'mpi': [258, 282, 164, 202, 322, 310, 231, 181],
}, {
    'time': '2013.5.5 21:14:44',
    'name': ['GODLIKE', '7LAN', 'BINGJR', 'LILI', 'MATT', 'INSPRATI'],
    'mpi': [325, 106, 117, 342, 407, 140],
}, {
    'time': '2013.5.5 21:15:30',
    'name': ['GODLIKE', 'INSPRATI', 'CAT', 'OOXXINC', 'UNRULY', 'MATT', 'MTH', 'BINGJR'],
    'mpi': [323, 293, 231, 265, 248, 319, 256, 202],
}, {
    'time': '2013.5.5 21:15:56',
    'name': ['INSPRATI', 'YUYU', '1234567', 'WSYGDBD', 'UNRULY', 'OOXXINC', 'LILI', 'KIRITO'],
    'mpi': [315, 234, 155, 266, 275, 291, 328, 287],
}, {
    'time': '2013.5.5 21:17:07',
    'name': ['GODLIKE', 'XIREN', 'INSPRATI', 'KIRITO', 'MATT', 'WH', 'FTD', 'FTD'],
    'mpi': [330, 134, 316, 156, 357, 167, 234, 178],
}, {
    'time': '2013.5.5 21:17:22',
    'name': ['ITSF8', 'MATT', 'YUYU', 'INSPRATI', 'GODLIKE', 'KIRITO', 'FTD'],
    'mpi': [226, 209, 142, 255, 270, 228, 245],
}, {
    'time': '2013.5.5 21:17:58',
    'name': ['DEROSA', 'XIREN', 'WOLEGEQU', 'AA', 'MATT', 'KIRITO', 'YL', 'UNRULY'],
    'mpi': [235, 266, 282, 293, 221, 265, 230, 257],
}, {
    'time': '2013.5.5 21:18:22',
    'name': ['KIRITO', 'OOXXINC', 'XIREN', 'FTD', 'PRATI', 'LILI', 'ITSF8', 'MATT'],
    'mpi': [224, 268, 175, 300, 250, 310, 211, 238],
}, {
    'time': '2013.5.5 21:18:37',
    'name': ['MATT', 'INSPRATI', 'XIREN', 'ITSF8', 'UNRULY', 'FTD', 'COLNAGO', 'KIRITO'],
    'mpi': [398, 315, 149, 315, 338, 395, 242, 364],
}, {
    'time': '2013.5.5 21:19:00',
    'name': ['MATT', 'GODLIKE', 'KIRITO', 'INSPRATI', 'YUYU', 'WYC', 'GIOS', 'FTD'],
    'mpi': [306, 346, 403, 239, 317, 136, 210, 393],
}, {
    'time': '2013.5.5 21:19:56',
    'name': ['UNRULY', 'INSPRATI', 'LILI', 'ITSF8', 'GODLIKE', 'VERDUROU', 'MATT', 'FTD'],
    'mpi': [238, 310, 407, 370, 407, 113, 458, 337],
}, {
    'time': '2013.6.28 21:06:14',
    'name': ['INSPRATI', 'KEVIN', 'OOXXINC', 'MATT'],
    'mpi': [244, 225, 266, 282],
}, {
    'time': '2013.6.28 21:45:32',
    'name': ['INSPRATI', 'OOXXINC', 'GODLIKE', 'HH', 'UNRULY', 'HHHHH'],
    'mpi': [206, 333, 291, 67, 97, 153],
}]


# generate weighted player indexes
def wpi(game):
    mpi = sorted(game['mpi'])
    weight = [1.] * len(mpi)
    rev_max_x = 1. / (len(mpi) - 1)

    for iteration in range(20):
        # calculate averages
        sum_x = 0.
        sum_y = 0.
        sum_weight = 0.
        for i in range(len(mpi)):
            sum_x += weight[i] * rev_max_x * i
            sum_y += weight[i] * mpi[i]
            sum_weight += weight[i]

        ave_x = sum_x / sum_weight
        ave_y = sum_y / sum_weight

        # calculate least squares
        diff_yx = 0.
        diff_yy = 0.
        for i in range(len(mpi)):
            diff_yx += weight[i] * (mpi[i] - ave_y) * (rev_max_x * i - ave_x)
            diff_yy += weight[i] * (mpi[i] - ave_y) ** 2

        k = diff_yx / diff_yy
        b = ave_x - k * ave_y

        # apply the results as new weights
        weight = [math.exp(k * i + b) for i in mpi]

    # calculate unsorted results
    game['wpi'] = [k * i + b for i in game['mpi']]


# calculate average indexes
def ave_wpi(data, init_lost=2.):
    players = set()
    for game in data:
        players |= set(game['name'])

    # calculate sums and counts
    sums = {i: 0. for i in players}
    counts = {i: 7. * init_lost for i in players}

    # load data from games
    for game in data:
        name = game['name']
        wpi = game['wpi']
        for i in range(len(wpi)):
            sums[name[i]] += (len(wpi) - 1) * wpi[i]
            counts[name[i]] += len(wpi) - 1

    # generate the results
    rank = {i: sums[i] / counts[i] for i in players}

    # sort the results
    return sorted(rank.items(), key=lambda x: x[1], reverse=True)


# generate Bradley-Terry Model ranks
def bt(data, init_lost=2., rank_diff=0.5):
    players = set()
    for game in data:
        players |= set(game['name'])

    # do log-likelihood solving
    rank = {i: 1. for i in players}
    for iteration in range(50):
        # new_rank_a = {i: 0. for i in players}
        # new_rank_b = {i: 0. for i in players}
        new_rank_a = {i: 0. for i in players}
        # assume lost $(init_lost) 8p games
        new_rank_b = {i: 7. * init_lost / (1. + rank[i]) for i in players}

        # load data from games
        for game in data:
            name = game['name']
            wpi = game['wpi']
            for i in range(len(wpi)):
                for j in range(len(wpi)):
                    if i != j:
                        wpi_diff = 0.5 * (1. - rank_diff) * (wpi[i] - wpi[j])
                        if wpi[i] > wpi[j]:
                            wpi_diff += 0.5 * rank_diff
                        else:
                            wpi_diff -= 0.5 * rank_diff

                        new_rank_a[name[i]] += 0.5 + wpi_diff
                        new_rank_a[name[j]] += 0.5 - wpi_diff

                        rev_rank = 1. / (rank[name[i]] + rank[name[j]])
                        new_rank_b[name[i]] += rev_rank
                        new_rank_b[name[j]] += rev_rank

        rank = {i: new_rank_a[i] / new_rank_b[i] for i in players}

        # normalize the results
        rev_ave_rank = len(rank) / sum(rank[i] for i in players)
        rank = {i: rev_ave_rank * rank[i] for i in players}

    # sort the results
    return sorted(rank.items(), key=lambda x: x[1], reverse=True)


for game in data:
    wpi(game)
    # print game['wpi']
print ave_wpi(data)
print
print bt(data)
