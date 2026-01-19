import os
import re

# --- START OF CONFIGURATION ---
# The full path to your website.html file
filepath = '/Users/thomas/Documents/mochi_claude/index.html'

# The list of new creators to add
new_creators = [
        
    {
        "name": "Joymei",
        "imageUrl": "https://img.coomer.st/thumbnail/data/1b/52/1b52b51879f3e8876fb8313101263aacd859e1eee8f20fcad29a4ae61edfa5b5.jpg",
        "backupImages": [
            "https://img.coomer.st/thumbnail/data/fa/b1/fab1a312b5047b7753d3dde5c6de56d06df047a889ce1fbe5124293fc7f6d261.jpg",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/CLoDwbAC#leALogaxjmjCmz_ZS_M3PQ",
        "linkvertiseUrl": "https://link-hub.net/1327817/NVFKJ9C6JjP7",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 21
    },
    {
        "name": "lwlrd444",
        "imageUrl": "https://fapodrop.com/images/-/-/3-lwlrd444/1/photo/3-lwlrd444_0011.jpeg",
        "backupImages": [
            "https://fapodrop.com/images/-/-/3-lwlrd444/1/photo/3-lwlrd444_0010.jpeg",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/WIozRDAZ#P4fQEap6eIgrhksSmvXzCg",
        "linkvertiseUrl": "https://link-hub.net/1327817/PkCbd4rHc2VP",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 14
    },
    {
        "name": "Peachytara",
        "imageUrl": "https://nudogram.com/contents/p/e/peachytara-1/1000/peachytara-1_0012.jpg",
        "backupImages": [
            "https://fr.leakedmodels.com/base/p/e/peachytara1/1000/peachytara1_0017.jpg",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/r2ZR1QjS#psXJcMXv0YDYFggYlRebVg/folder/PyInmLpZ",
        "linkvertiseUrl": "https://link-target.net/1327817/43a3KXsYopik",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 8
    },
    {
        "name": "Viviannn_cc",
        "imageUrl": "https://img.coomer.st/thumbnail/data/8e/d8/8ed8115a311bed5b4ffc04edd161f6a94c9b7ce02f3d06e46ea1ebbffa3560e7.jpg",
        "backupImages": [
            "https://img.coomer.st/thumbnail/data/e8/0e/e80e52b348215f7f339de5981b1ff5c2fb3b3b8b6a4703ab57e17192e16c4936.jpg",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/6N5TSQ7A#Je0leqnSiVrEf6McawLZNA",
        "linkvertiseUrl": "https://link-center.net/1327817/x5EBXvBjFIMa",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 32
    },
    {
        "name": "Phoeyuibe",
        "imageUrl": "https://pbs.twimg.com/media/FXnuv22WQAIN7Eh.jpg",
        "backupImages": [
            "https://nudogram.com/contents/p/h/phoeyuibe/1000/phoeyuibe_0152.jpg",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/WJsUUDjD#Bh9OQdo3XbEd98qMyKdezA",
        "linkvertiseUrl": "https://link-center.net/1327817/SoB6tH56evgl",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 29
    },
    {
        "name": "Astrid",
        "imageUrl": "https://fapodrop.com/images/s/e/serveastrid/1/photo/serveastrid_0001.jpeg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/hFR1BThS#KyX3NM9GM7lNzPbdN4F1RA",
        "linkvertiseUrl": "https://link-center.net/1327817/zPzywV7ixjhq",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 3
    },
    {
        "name": "Yemada",
        "imageUrl": "https://i0.wp.com/cdn.beacons.ai/user_content/PsAVUNjX7wSq0bfnHQwqploWO2H3/profile_yemadajpeg.png?w=600",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/KlolXY7I#U1SKrFAZYy8cEmWQBg4pHA/folder/qg5wGawC",
        "linkvertiseUrl": "https://link-center.net/1327817/QN3gf6e0w8Zb",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 18
    },
    {
        "name": "SpicyLittleBunny",
        "imageUrl": "https://img.coomer.st/thumbnail/data/e9/9a/e99a4aa0c616348694f263ca73dfeb53cb83a0ad6d787df7ae992cef6064522e.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/iLwRQYaK#oBOskMnjuiTz83q_915csw",
        "linkvertiseUrl": "https://link-center.net/1327817/uGZnRbQFhoka",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 7
    },
    {
        "name": "abgbunnyy",
        "imageUrl": "https://img.coomer.st/thumbnail/data/44/29/44295b888db526236b25bb38c8079c24fa79eeb3247a68d015da51750b9d1b96.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/KtREnTwI#YGxRTYjBspe_K8_JR9mIhA",
        "linkvertiseUrl": "https://direct-link.net/1327817/kiRxR8cbSjP9",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 25
    },
    {
        "name": "bunnybrownie36",
        "imageUrl": "https://nudogram.com/contents/b/u/bunnybrownie/1000/bunnybrownie_0216.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/h6FRGYoZ#6SLyjhecmS17yBGsouUGKg",
        "linkvertiseUrl": "https://link-hub.net/1327817/VqAhfbgQDBri",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 16
    },
    {
        "name": "Irisadamsone",
        "imageUrl": "https://img.coomer.st/thumbnail/data/de/a5/dea586bdc64a21331b4928018e765c276bf70d06bdef9ea80a4073c1811e9128.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/DdMyAawK#ZlxMfCehWrRQl2BfEpXDHQ",
        "linkvertiseUrl": "https://direct-link.net/1327817/yQHwfK0P0ySN",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 11
    },
    {
        "name": "Briddyli",
        "imageUrl": "https://nudogram.com/contents/b/r/briddy-li/1000/briddy-li_0026.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/eZF3jQqZ#xXaoqqAxpNbvGVclxAb94g/folder/DdswXQDY",
        "linkvertiseUrl": "https://link-center.net/1327817/pIN5bUPC6K8M",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 9
    },
    {
        "name": "Kellie",
        "imageUrl": "https://thumbs2.imgbox.com/6c/6d/GfI02yek_t.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/igwzFbDB#c9iXt1z14gAQ6r0jSyzsQQ",
        "linkvertiseUrl": "https://link-target.net/1327817/Tk3RrWeZ7VWa",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 4
    },
    {
        "name": "Millie Cha",
        "imageUrl": "https://i0.wp.com/masterfap.net/profile/milliecha/photos/dhHAvHerys/milliecha.webp?w=600",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/O0QU3K6a#lqNvPbUSyQxn47_UsjqeLQ",
        "linkvertiseUrl": "https://direct-link.net/1327817/GjpHxdH0jeSb",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 30
    },
    {
        "name": "mizukawasumire",
        "imageUrl": "https://img.coomer.st/thumbnail/data/e7/cf/e7cfdd2918824435d3f631e1937c62b393a528b9dd132f410ea839f07009cde5.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/CAgTQSyB#5vlS24DxLrVcRuiQRVMrHA",
        "linkvertiseUrl": "https://direct-link.net/1327817/anmbvUROdj8R",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 22
    },
    {
        "name": "AthenaNavy",
        "imageUrl": "https://nudogram.com/contents/a/t/athena-navy/1000/athena-navy_0034.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/p38iARQL#hFdVkN3kwUyeCJ4SEVhKQA",
        "linkvertiseUrl": "https://link-hub.net/1327817/G8jajrYYfP4t",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 15
    },
    {
        "name": "Kiri Amari",
        "imageUrl": "https://nudogram.com/contents/k/i/kiri-amari/1000/kiri-amari_0182.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/qpQgnJAA#TIDL_mpR9uTCNn_6c5c33w",
        "linkvertiseUrl": "https://link-center.net/1327817/64itCVcKyBaK",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 27
    },
    {
        "name": "Michelle ngo",
        "imageUrl": "https://thumbs2.imgbox.com/cd/3d/3tRevNpf_t.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/3BhimDaa#r6BcxKfUoO8bSwWUX0z6Gw",
        "linkvertiseUrl": "https://direct-link.net/1327817/fJYiHEnyWBht",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 2
    },
    {
        "name": "MINAASH",
        "imageUrl": "https://fapodrop.com/images/-/-/4-minaashfree/1/photo/4-minaashfree_0001.jpeg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/CxQFhTwS#1cka0A57N_SVjPMxbrzC7g",
        "linkvertiseUrl": "https://link-center.net/1327817/HpMaR2wha3pV",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 19
    },
    {
        "name": "hibellanicole",
        "imageUrl": "https://img.coomer.st/thumbnail/data/1a/20/1a20b76e05aa17b82474f6c0caedbad3ebde2946c3c4765e336ab761535bcd8c.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/n5xByDAT#RBBYJal2nqimGYgvumTM2g",
        "linkvertiseUrl": "https://link-target.net/1327817/HlDRD832QDaY",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 6
    },
    {
        "name": "HaloCoco",
        "imageUrl": "https://img.coomer.st/thumbnail/data/6e/26/6e2658b16266b2fbc5f4d05df7281aa2f3ee71498303858ec4c81569e84bfa9f.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/Knh2kDRa#N8NwAdD0OioyDFO6THXaIg/folder/3qwQDBxa",
        "linkvertiseUrl": "https://link-hub.net/1327817/C3huigOKO0Qd",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 34
    },
    {
        "name": "Kharismatic",
        "imageUrl": "https://nudogram.com/contents/k/h/kharismatic-1/1000/kharismatic-1_0020.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/3AIXCC6R#akDCXqDVYrEaxinTUpIkFA",
        "linkvertiseUrl": "https://link-center.net/1327817/NYXilSejgirr",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 13
    },
    {
        "name": "SophieRain",
        "imageUrl": "https://fapodrop.com/images/s/o/sophierain/1/photo/sophierain_0011.jpeg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/5tRUXCQJ#olTZZRO4Pq7153QLKGoLOA",
        "linkvertiseUrl": "https://link-center.net/1327817/RrXm8jNtiLzK",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 26
    },
    {
        "name": "Ppwyang0",
        "imageUrl": "https://nudogram.com/contents/p/p/ppwyang0-1/1000/ppwyang0-1_0040.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/0mlETSYb#UOpPSmOxcy4pTm65qPiWPg",
        "linkvertiseUrl": "https://link-hub.net/1327817/t2bF4iEyOMEz",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 17
    },
    {
        "name": "Lenerox",
        "imageUrl": "https://img.coomer.st/thumbnail/data/7a/41/7a416aa8e6dbe25ef4908f13c63ea1db956b0e749aaae61f2543e438ce852ebc.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/KORRiDyT#bvKCzKoMUeG59nR1wGlmAQ",
        "linkvertiseUrl": "https://direct-link.net/1327817/UI5UTZgupJE9",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 10
    },
    {
        "name": "Calamari.mami",
        "imageUrl": "https://nudogram.com/contents/c/a/calamari-mami/1000/calamari-mami_0050.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/LlgVSZxa#7ChrVpcIPHFgSIOM6mmSvw/folder/rx5FXILJ",
        "linkvertiseUrl": "https://link-target.net/1327817/NDtAVgDg1GSk",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 23
    },
    {
        "name": "kawaiisofey",
        "imageUrl": "https://img.coomer.st/thumbnail/data/f4/c7/f4c7c4bcbe2478e8532fe7a6ab18ffc75218f78653539a782dece34becc0d271.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/aGRg3TwZ#3NyqOHOWYz66zR8yThMZZQ/folder/OW4hVb6S",
        "linkvertiseUrl": "https://link-target.net/1327817/NpIdOhCK49bH",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 31
    },
    {
        "name": "Martina chen",
        "imageUrl": "https://simp6.selti-delivery.ru/images3/IMG_3690f2d0d2ab48e8e6cb.md.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/v0ZRzI4Y#A6DWY1ol4YT_Ydmbu8NnnA",
        "linkvertiseUrl": "https://direct-link.net/1327817/phWwk5sRLFZo",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 5
    },
    {
        "name": "Babietayy",
        "imageUrl": "https://nudogram.com/contents/b/a/babietayy/1000/babietayy_0002.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/1blAHAja#xfG27EbhbpodbUONVciIuw/folder/AasiRSYZ",
        "linkvertiseUrl": "https://link-target.net/1327817/5ZIvO5OE1rXN",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 12
    },
    {
        "name": "Foopahh",
        "imageUrl": "https://i0.wp.com/image-cdn.hotleaks.tv/storage/images/4ab/f8416f/f8416f.webp?w=600",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/0vI21IaL#DO4OFlvPhH-VXxNEYm5DEA",
        "linkvertiseUrl": "https://direct-link.net/1327817/yYV2IGIwFbnE",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 20
    },
    {
        "name": "Yunseo",
        "imageUrl": "https://jpg6.su/img/1000450112.aP1BSXI",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/LponQRZK#1-v9fifRfCYjeqpEy7zexA",
        "linkvertiseUrl": "https://link-hub.net/1327817/pA0RW5qcioNl",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 28
    },
    {
        "name": "Msbreewc",
        "imageUrl": "https://nudogram.com/contents/b/r/bree-wales-covington/1000/bree-wales-covington_0067.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/XvZzEQ5B#GSPY9kwlM6XaTVT3uhrDKg",
        "linkvertiseUrl": "https://link-target.net/1327817/a8kykThSOjpT",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 9
    },
    {
        "name": "Kittynobi",
        "imageUrl": "https://nudogram.com/contents/k/i/kittynobi-1/1000/kittynobi-1_0003.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/CyJxmTqZ#PJSn1Gb0E1C81D3NsxR__A/folder/i2ZRyJ4D",
        "linkvertiseUrl": "https://direct-link.net/1327817/UdJtvMO7hMe4",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 33
    },
    {
        "name": "Lillienue",
        "imageUrl": "https://img.coomer.st/thumbnail/data/d4/5d/d45dca0b49b25bef407bb8fcbbb3d53f5dc4a116b4b1140761bd1185b96ccf66.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/scFUGbjD#TQZ_120CPwRB7kUfAWXtcw/folder/wdl2mZYY",
        "linkvertiseUrl": "https://link-hub.net/1327817/rIHxZLEniSMC",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 1
    },
    {
        "name": "babyakira",
        "imageUrl": "https://img.coomer.st/thumbnail/data/75/36/75360f47e1abe32cfe633f45b1bccabc4e41282b28b5acd38dfdb0fa2b753c89.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/qY0nCAaI#70FbpI4BCq_mfF6NzEvI0A/folder/jNtGHQ7b",
        "linkvertiseUrl": "https://direct-link.net/1327817/69YWIsIwG1i0",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 14
    },
    {
        "name": "Thiccasianbaddie",
        "imageUrl": "https://fapello.com/content/c/h/christie-anne-13/1000/christie-anne-13_0002.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/aM9RmTjT#NbHQjYsLZ48VzbHHhGiMQ/folder/HU8AHBKb",
        "linkvertiseUrl": "https://direct-link.net/1327817/QivKB37PxSCu",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 8
    },
    {
        "name": "Vietwhore",
        "imageUrl": "https://fapello.com/content/v/i/vietwhore/1000/vietwhore_0001.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/fFNiiLYI#_P6ZKniGMF3GVt-35KhSVA",
        "linkvertiseUrl": "https://direct-link.net/1327817/PDkocFoVgenY",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 29
    },
    {
        "name": "Madison.ellee",
        "imageUrl": "https://img.coomer.st/thumbnail/data/fc/86/fc860555b42e3da755713143d386ac1ef7be75c4cb156854c4e3d8c423580650.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/cudzgQga#qzrDY0vY4OuQPbDeziVm1g",
        "linkvertiseUrl": "https://link-hub.net/1327817/kY48Dmt9Q83q",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 16
    },
    {
        "name": "Misscindy",
        "imageUrl": "https://nudogram.com/contents/m/i/misscindyy/1000/misscindyy_0122.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/qj5CkQpQ#Xxb2OsS_xqKvAQeluRRzDw/folder/iz5zTZoa",
        "linkvertiseUrl": "https://link-target.net/1327817/mVPysM3Pr2c7",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 24
    },
    {
        "name": "Mspuiyi",
        "imageUrl": "https://img.coomer.st/thumbnail/data/1c/37/1c372c9f67895a1e0d648d4b99e58419f03d693b39962d6cff7d2e5f189d6deb.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/zZtEESRQ#lSQWlvHqmMWv6MIR_ia-TQ/folder/DUEQWLbb",
        "linkvertiseUrl": "https://direct-link.net/1327817/5AHgUBrRlQPk",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 11
    },
    {
        "name": "Jezzi xo",
        "imageUrl": "https://fapeza.com/media/j/e/jezzi-xo-25/1000/jezzi-xo-25_0042.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/Wio2iRLC#gl61Eukj8mQmDEYVt6tSYQ",
        "linkvertiseUrl": "https://link-hub.net/1327817/m0dreZCxwHW5",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 19
    },
    {
        "name": "Cannabunni3",
        "imageUrl": "https://fapeza.com/media/c/a/cannabunni3/1000/cannabunni3_0099.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/i8B3CRDC#4OljVLalacPS0Jz0VDEeng/folder/u1AkFTLJ",
        "linkvertiseUrl": "https://link-target.net/1327817/RI9CA7Pt1ymE",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 27
    },
    {
        "name": "Taylorafterdark",
        "imageUrl": "https://jpg6.su/img/tvylorafterdark-image-056.a1hDjU1",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/2kJVkT5C#Di8GDWdtmog9ASIjX_eaSg/folder/jlgWlTqB",
        "linkvertiseUrl": "https://link-target.net/1327817/qKMCI9xc76og",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 5
    },
    {
        "name": "Itsrosebby",
        "imageUrl": "https://nudogram.com/contents/i/t/itsrosebbyx/1000/itsrosebbyx_0019.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/3NxBgArb#QAeGQ922eLCqefB9G3a8YA/folder/aQgHCIyT",
        "linkvertiseUrl": "https://link-center.net/1327817/IGgk4fMULEA0",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 13
    },
    {
        "name": "Kaile Goh",
        "imageUrl": "https://i0.wp.com/fapellas.com/data/k/a/kaile-goh-1/1000/kaile-goh-1_0006.jpg?w=600",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/2ipCxYwJ#AR88TP1TgRU1WaZwluis8Q",
        "linkvertiseUrl": "https://link-center.net/1327817/u80OW3kFwya2",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 30
    },
    {
        "name": "Nikita Kim",
        "imageUrl": "https://jpg6.su/img/nikitacruze-pics-14.B2itu9",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/dmkA1LJI#tX5GEDW68qwtxCOoqKiscg",
        "linkvertiseUrl": "https://link-center.net/1327817/KkusABbvva4I",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 22
    },
    {
        "name": "Niykiii Namaste",
        "imageUrl": "https://nudogram.com/contents/n/i/niykiiinamaste/1000/niykiiinamaste_0035.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/ZC0llZYa#2opA56uUghLPMEAF_5aQwg",
        "linkvertiseUrl": "https://direct-link.net/1327817/1sc0VUhnnU2s",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 4
    },
    {
        "name": "Junoave",
        "imageUrl": "https://jpg6.su/img/6c95457f-237f-432e-a27d-2830bfd59989.H4wtlg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/CxxUCQwJ#3YvbL8wvtnnQx4KPxd3Tsg",
        "linkvertiseUrl": "https://link-center.net/1327817/qez8XFGtifF6",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 18
    },
    {
        "name": "Aroomi Kim",
        "imageUrl": "https://nudogram.com/contents/a/r/aroomi-kim/1000/aroomi-kim_0106.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/QVZFxY4b#7NpFNojOpQk0Ff1swLh5cQ",
        "linkvertiseUrl": "https://link-center.net/1327817/dom2d4odHY9R",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 7
    },
    {
        "name": "VandalBunnie",
        "imageUrl": "https://nudogram.com/contents/v/a/vandalbunnie/1000/vandalbunnie_0085.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/MvpRTDiA#ItoWTJOnOB12z_Ul4NWn9w",
        "linkvertiseUrl": "https://link-hub.net/1327817/r6vxDGxT5b1f",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 32
    },
    {
        "name": "Hanna aiyuens",
        "imageUrl": "https://thumbs2.imgbox.com/6d/c2/udKukf4l_t.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/1UgVBQYR#K_9awQ62ic9VuPLdcnLwJA",
        "linkvertiseUrl": "https://link-target.net/1327817/8Lr6fyeFxiE7",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 15
    },
    {
        "name": "kannasuku",
        "imageUrl": "https://nudogram.com/contents/k/a/kannasuku/1000/kannasuku_0264.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://bunkr.cr/a/qnAsGZ3a",
        "linkvertiseUrl": "https://direct-link.net/1327817/2DxWiQzsJq1Y",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 6
    },
    {
        "name": "ZOL8YCK",
        "imageUrl": "https://nudogram.com/contents/n/e/nejisui/1000/nejisui_0041.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/vQggAJob#RvzcEcbKwe3AFYSu0Xc39g",
        "linkvertiseUrl": "https://link-hub.net/1327817/bqXZ6b2No1AI",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 25
    },
    {
        "name": "QueenOfNeko",
        "imageUrl": "https://nudogram.com/contents/q/u/queenofneko/1000/queenofneko_0030.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/vEEHwRbB#e7O_BFkkxthVHM0giJnOog/folder/DN0CABqa",
        "linkvertiseUrl": "https://link-hub.net/1327817/8aNn7PzKKCHQ",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 3
    },
    {
        "name": "sophiasummers1",
        "imageUrl": "https://fapello.com/content/s/o/sophiasummers1-2/1000/sophiasummers1-2_0058.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/VMIljRaJ#OTP5egbYZj_FCC4DmNpTzw",
        "linkvertiseUrl": "https://link-target.net/1327817/7k2xxYjuGjBh",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 12
    },
    {
        "name": "Toriiilee",
        "imageUrl": "https://fapello.com/content/t/o/toriiilee/1000/toriiilee_0008.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/A2h10ISJ#xqjW7eKKQT2qADAsxhKZPg",
        "linkvertiseUrl": "https://link-target.net/1327817/is11eVTrBIcf",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 17
    },
        {
        "name": "Callmecupcakes",
        "imageUrl": "https://nudogram.com/contents/c/a/callmecupcakes/1000/callmecupcakes_0023.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/f7giTBwC#H0drUxO6EORx2VyTJT4OZA/folder/njBnDRqL",
        "linkvertiseUrl": "https://link-target.net/1327817/Ks7yJKx0mabJ",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 9
    },
    {
        "name": "Juneliu",
        "imageUrl": "https://img.coomer.st/thumbnail/data/b8/80/b880d6598d73e0be73d29ef7e3aa2261ec93783187a8292fe3362b16b40bc022.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/uZtAUSjA#FSZg_E9SekdTU1nb32Anbg",
        "linkvertiseUrl": "https://link-center.net/1327817/MlyBwm8LWYQi",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 21
    },
    {
        "name": "Sxilorpluto",
        "imageUrl": "https://i0.wp.com/image-cdn.hotleaks.tv/storage/images/89a0/f2a751/f2a751.webp?w=600",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/NsYhlBqb#N4RMtSYxic_ZZVCNnzECqg",
        "linkvertiseUrl": "https://direct-link.net/1327817/pMXFN5JPin4n",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 14
    },
    {
        "name": "diakimeko",
        "imageUrl": "https://i0.wp.com/image-cdn.hotleaks.tv/storage/images/90eb/f306aa/f306aa.webp?w=600",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/vSIhHRTA#QhTQgaePqF0cZHA8C2g52g",
        "linkvertiseUrl": "https://link-center.net/1327817/rOwABGCsPJyi",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 33
    },
    {
        "name": "Ilysmkei",
        "imageUrl": "https://nudogram.com/contents/i/l/ilysmkei-1/1000/ilysmkei-1_0100.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/KQUyVCoY#QFVc0q_rW6Juukd6ENCxDw/folder/6Y8CWRRQ",
        "linkvertiseUrl": "https://link-target.net/1327817/e4bbveWMcUAH",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 5
    },
    {
        "name": "Stepsisterangela",
        "imageUrl": "https://i0.wp.com/image-cdn.hotleaks.tv/storage/images/b5a/113550/113550.webp?w=600",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/ZnBSwaqT#NAW_bzpsuWwz8Hu_Nk0qCw",
        "linkvertiseUrl": "https://link-hub.net/1327817/iU3RZcuBw4yE",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 11
    },
    {
        "name": "Asianfreshman",
        "imageUrl": "https://img.coomer.st/thumbnail/data/51/b0/51b0e00dfab430aeb510944ee8c8087edadebfec8bc0a78d2dda56c56b96e428.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/CtpBBYbS#1rmZ7C58CkFtKIRV1fkvCA",
        "linkvertiseUrl": "https://link-hub.net/1327817/DIVlZx7kk82H",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 26
    },
    {
        "name": "Alyvxo",
        "imageUrl": "https://nudogram.com/contents/a/l/alyvxo/1000/alyvxo_0063.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/iFV3iKKL#JxpSZNw42ELHXHkRULlM1Q",
        "linkvertiseUrl": "https://direct-link.net/1327817/6fEzjIUbBNda",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 19
    },
    {
        "name": "Icybabym",
        "imageUrl": "https://nudogram.com/contents/i/c/icybabym/1000/icybabym_0023.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/BIwXBTwL#3b7TtPkgKHsJTixyKU3oxg/folder/1AwFwDZZ",
        "linkvertiseUrl": "https://direct-link.net/1327817/ajNcKMYgDW5e",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 8
    },
    {
        "name": "Taylor",
        "imageUrl": "https://nudogram.com/contents/t/v/tvylorafterdark-1/1000/tvylorafterdark-1_0107.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/SOowwS7C#3XzxRIs8uKmG8btHQMHpMQ",
        "linkvertiseUrl": "https://link-hub.net/1327817/rinGQ2KP7bpc",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 15
    },
    {
        "name": "Sashahu",
        "imageUrl": "https://nudogram.com/contents/s/a/sashahu/1000/sashahu_0007.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/EBk2URjA#fKRTa8wTliKvo9mPLPVBpw/folder/pBkFkaBY",
        "linkvertiseUrl": "https://link-center.net/1327817/FICq2m5nMVCq",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 2
    },
    {
        "name": "Mxckeymeiji",
        "imageUrl": "https://i0.wp.com/masterfap.net/profile/mxckeymeiji/photos/smHtrfgnLo/mxckeymeiji.webp?w=600",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/mI9E0KIS#KPd1n7cXbWWyheaB-AWrHA/folder/TIEigLxS",
        "linkvertiseUrl": "https://link-hub.net/1327817/i4QMliDZiGmQ",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 30
    },
    {
        "name": "Babiebeezz",
        "imageUrl": "https://fapeza.com/media/b/a/babiebeezz/1000/babiebeezz_0032.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/6ZlWCa6J#QPAF9UWoPdin8hviTgmj3A",
        "linkvertiseUrl": "https://direct-link.net/1327817/0pBVIAv6C6Vg",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 23
    },
    {
        "name": "Maypowpow",
        "imageUrl": "https://jpg6.su/img/960x960-6048608444b1f3ecbaa019a9c79e2300.atZiyPS",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/MsRR1R4B#FjNfwZBQOj1rBW0KwiWP7Q",
        "linkvertiseUrl": "https://link-center.net/1327817/yELVLkqxSPYm",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 7
    },
    {
        "name": "Erzabel",
        "imageUrl": "https://img.coomer.st/thumbnail/data/80/f6/80f6ab259a39cdd26e2789fe89743be1b1c287b1a920de490635817fe9978c12.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/bYUHzY5J#goPBjIwoZiO106PHT27Rzg",
        "linkvertiseUrl": "https://link-target.net/1327817/2jXYTfzNFGBC",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 17
    },
    {
        "name": "Qilin.anh",
        "imageUrl": "https://fapeza.com/media/q/i/qilin-anh-22/1000/qilin-anh-22_0114.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/Uv9myZaS#7kt1XtAggJaLSeWB_w7FtQ/folder/RvsU1ABR",
        "linkvertiseUrl": "https://link-target.net/1327817/dxE1vREH9eNm",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 31
    },
    {
        "name": "Sophie rain",
        "imageUrl": "https://nudogram.com/contents/s/o/sophie-rain-1/1000/sophie-rain-1_0072.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/GQkFFBDS#8RrhURIdrp7S9MpOTU49oA/folder/yZtS3BBZ",
        "linkvertiseUrl": "https://link-center.net/1327817/zRVG7A8D0PUz",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 6
    },
    {
        "name": "Victoriamezei",
        "imageUrl": "https://fapello.com/content/v/i/victoriamezei-7/1000/victoriamezei-7_0026.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/6cFyxAiB#GtDtrTSGIKv7kyMlxSMnNw",
        "linkvertiseUrl": "https://link-hub.net/1327817/RcO7aArO8pIg",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 12
    },
    {
        "name": "Meowbarbie",
        "imageUrl": "https://fapello.com/content/m/e/meowbarbie-8/1000/meowbarbie-8_0018.jpg",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/mnQgBYCC#2mNRrrgHcNozY5hTfZL2nQ/folder/z7QGWByT",
        "linkvertiseUrl": "https://link-hub.net/1327817/wkHDyu05Afzb",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 28
    },
    {
        "name": "Jess kim",
        "imageUrl": "https://jpg6.su/img/0008.xaLICD",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/aI8AxZoL#KR6Ofj2xKtejgcBKNS4EZg",
        "linkvertiseUrl": "https://link-center.net/1327817/3aAaAlAqQEuP",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 4
    },
    {
        "name": "Lauren jasmine",
        "imageUrl": "https://pbs.twimg.com/media/F5MdjZRasAAtXh8.jpg:small",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/IRBx1YbT#nDswYE8OqUMlVA2eiUAslw",
        "linkvertiseUrl": "https://link-hub.net/1327817/bnZh9jXRgZyJ",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 20
    },
    {
        "name": "Lolavalentinexoxo",
        "imageUrl": "https://i0.wp.com/fapellas.com/data/l/o/lolavalentinexoxo/1000/lolavalentinexoxo_0003.jpg?w=600",
        "backupImages": [
            "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
            "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
        ],
        "contentUrl": "https://mega.nz/folder/2RlQgBoY#V0CG_xQyUHd0_1VfRhWcAg",
        "linkvertiseUrl": "https://link-target.net/1327817/5P6mp7waq9LT",
        "description": "",
        "addedDate": "2025-01-06T10:00:00.000Z",
        "baseViews": 13
    },
    {
    "name": "Lyla fit",
    "imageUrl": "https://img.coomer.st/thumbnail/data/50/fb/50fb937d4260cadf2c2b6460ff80ebdd0f8d5d2e4b7b1de00a73d35b701aaf98.jpg",
    "backupImages": [
        "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1",
        "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2"
    ],
    "contentUrl": "https://mega.nz/folder/HA1hRCzb#kwdhQzHIeXi039Rm1ymsDQ",
    "linkvertiseUrl": "https://link-hub.net/1327817/8DNW448RCxrb",
    "description": "",
    "addedDate": "2025-01-06T10:00:00.000Z",
    "baseViews": 22
    }
        
    
]
# --- END OF CONFIGURATION ---


# --- DO NOT EDIT BELOW THIS LINE ---
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the start of the leftColumn array to insert new creators
    left_column_start = content.find('"leftColumn": [')
    if left_column_start == -1:
        raise ValueError("Could not find 'leftColumn' in the HTML file.")

    insert_position = content.find('[', left_column_start) + 1
    new_entries_js = ""

    # Loop through the new creators and generate their JavaScript object strings
    for creator in new_creators:
        # Sanitize creator name for regex pattern matching
        safe_name = re.escape(creator['name'])
        
        # Remove any existing entry for this creator to avoid duplicates
        old_creator_pattern = re.compile(
            r'\{[^^}]*"name":\s*"' + safe_name + r'"[^^}]*\}},?\s*\n?',
            re.DOTALL
        )
        content = old_creator_pattern.sub('', content)

        # Create the JavaScript object string for the new creator
        new_entries_js += f"""
        {{ "name": "{creator['name']}", "imageUrl": "{creator['imageUrl']}", "backupImages": [ "https://via.placeholder.com/400x400/00aff0/ffffff?text=Backup+1", "https://via.placeholder.com/400x400/018cf1/ffffff?text=Backup+2" ], "contentUrl": "{creator['contentUrl']}", "linkvertiseUrl": "{creator['linkvertiseUrl']}", "description": "", "addedDate": new Date().toISOString() }},"""

    # Insert all new entries at the top of the leftColumn
    content = content[:insert_position] + new_entries_js + content[insert_position:]

    # Write the modified content back to the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'✅ Success! File updated: website.html')
    print(f'📁 Location: {filepath}')
    print(f'Added {len(new_creators)} new creators to the top of the list.')

except FileNotFoundError:
    print(f"❌ Error: The file was not found at the specified path.")
    print(f"Please check if this path is correct: {filepath}")
except Exception as e:
    print(f'❌ An error occurred: {e}')
