username = ***
password = ***

import pymongo

client = pymongo.MongoClient("mongodb://lotta01:<PASSWORD>@lotta3-shard-00-00-qnrwa.mongodb.net:27017,lotta3-shard-00-01-qnrwa.mongodb.net:27017,lotta3-shard-00-02-qnrwa.mongodb.net:27017/test?ssl=true&replicaSet=lotta3-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

armory_item = [
    {
        "item_id": 1,
        "name": "Libero facere dolore, as",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 2,
        "name": "Qui",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 3,
        "name": "Laborios",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 4,
        "name": "Quibusdam illo deserunt ea",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 5,
        "name": "Quod eveniet i",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 6,
        "name": "Qui odio beata",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 7,
        "name": "Omnis",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 8,
        "name": "Saepe ea vo",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 9,
        "name": "Vel illo sed",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 10,
        "name": "Pariatur hic iste m",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 11,
        "name": "Eum illo expedita",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 12,
        "name": "Laudantium recusand",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 13,
        "name": "Molesti",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 14,
        "name": "Veniam fuga n",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 15,
        "name": "Animi molestias possimus nihil",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 16,
        "name": "Assu",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 17,
        "name": "Officiis",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 18,
        "name": "Consectetur deleniti cupi",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 19,
        "name": "Explicabo",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 20,
        "name": "Dolores rem v",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 21,
        "name": "Sit rerum err",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 22,
        "name": "Sapiente numquam qu",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 23,
        "name": "Nam ab illum culpa corporis fu",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 24,
        "name": "Blanditiis obcaecat",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 25,
        "name": "Ex",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 26,
        "name": "Assumenda nam i",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 27,
        "name": "Distinctio mini",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 28,
        "name": "Impedit libero id modi eos vol",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 29,
        "name": "In p",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 30,
        "name": "Possimus quae elig",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 31,
        "name": "Vitae nulla praesentium magnam",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 32,
        "name": "Ipsam placeat e",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 33,
        "name": "Corporis ani",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 34,
        "name": "Eius cum quis",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 35,
        "name": "Suscip",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 36,
        "name": "Soluta consequatur dolore",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 37,
        "name": "Perferendis corr",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 38,
        "name": "Reprehen",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 39,
        "name": "Eveniet impedi",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 40,
        "name": "Accusamus reprehenderit beata",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 41,
        "name": "Beatae do",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 42,
        "name": "Error maiores nulla",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 43,
        "name": "Tempore",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 44,
        "name": "Culpa nemo vol",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 45,
        "name": "Repellat iusto quam reprehen",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 46,
        "name": "Exp",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 47,
        "name": "Animi dolor at est",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 48,
        "name": "Labore a consecte",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 49,
        "name": "Sed quo corpor",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 50,
        "name": "Officia asperiores obcaecati d",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 51,
        "name": "Ipsam",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 52,
        "name": "Molestiae veniam",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 53,
        "name": "Perferendis repudiandae labo",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 54,
        "name": "Similique totam quasi ipsa ex",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 55,
        "name": "Velit voluptatem",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 56,
        "name": "Harum voluptatum ius",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 57,
        "name": "Ex libero soluta",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 58,
        "name": "Quos re",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 59,
        "name": "Deleniti quas explica",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 60,
        "name": "Porro molliti",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 61,
        "name": "Enim laboriosam quae",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 62,
        "name": "Natus rem repellat quas assum",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 63,
        "name": "Quasi re",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 64,
        "name": "Laudantium c",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 65,
        "name": "Quos blanditiis nost",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 66,
        "name": "Quisquam ut cupiditate",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 67,
        "name": "Eaque nemo velit nece",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 68,
        "name": "Repudiandae",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 69,
        "name": "Minus illum vo",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 70,
        "name": "Minus repell",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 71,
        "name": "Quia quasi labo",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 72,
        "name": "Eligendi fuga mol",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 73,
        "name": "Beatae ita",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 74,
        "name": "Quo sunt laudantium al",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 75,
        "name": "Ist",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 76,
        "name": "Voluptatem laborum dicta cum",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 77,
        "name": "Corporis obcaecati ven",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 78,
        "name": "Neque quae eum dign",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 79,
        "name": "Dolorem quam neque, amet cum e",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 80,
        "name": "Rem expedit",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 81,
        "name": "Est sapiente iusto minus quam",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 82,
        "name": "Atque laudantium dolor q",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 83,
        "name": "Accusan",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 84,
        "name": "Consectetur error o",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 85,
        "name": "Alias laboriosam sapiente e",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 86,
        "name": "Doloribus animi perspiciatis",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 87,
        "name": "Hic possimus qua",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 88,
        "name": "Unde quaerat tenetur",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 89,
        "name": "Facere reprehenderit v",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 90,
        "name": "Aperiam consequuntu",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 91,
        "name": "Quis expedita ip",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 92,
        "name": "Ea vel deserunt aspernat",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 93,
        "name": "Natus",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 94,
        "name": "Optio iusto laboriosam te",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 95,
        "name": "Laborios",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 96,
        "name": "Commodi deserunt in illo",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 97,
        "name": "Ad numquam dicta cons",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 98,
        "name": "Aliquid aliquam velit reru",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 99,
        "name": "Facere q",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 100,
        "name": "Incidunt libero assumen",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 101,
        "name": "Earum suscipit ea voluptates i",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 102,
        "name": "Sint dolorum",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 103,
        "name": "Incidunt fugiat ea, ea",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 104,
        "name": "Molestiae r",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 105,
        "name": "Voluptatem labore laboriosa",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 106,
        "name": "Et ducimus cumque aut perspic",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 107,
        "name": "Corrupti ap",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 108,
        "name": "Perferendis nesciunt quae dolo",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 109,
        "name": "Sunt doloremque recusanda",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 110,
        "name": "Deleniti similique obc",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 111,
        "name": "Numquam tempor",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 112,
        "name": "Quibusdam deleniti quasi provi",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 113,
        "name": "Accusamus exercitat",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 114,
        "name": "Error eveniet ipsum, expedi",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 115,
        "name": "Sapiente do",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 116,
        "name": "Fuga necessitatibus",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 117,
        "name": "Nam excepturi placeat asperna",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 118,
        "name": "Dolore fugit itaq",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 119,
        "name": "Beatae ve",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 120,
        "name": "Blanditiis corporis exerci",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 121,
        "name": "Nesciunt quia nobi",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 122,
        "name": "Quisquam e",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 123,
        "name": "Illo q",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 124,
        "name": "Repellat voluptates ea,",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 125,
        "name": "Labore architecto tempora d",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 126,
        "name": "Porro impedit enim earum nam n",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 127,
        "name": "Evenie",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 128,
        "name": "Similique do",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 129,
        "name": "Quos voluptates at n",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 130,
        "name": "Neq",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 131,
        "name": "Neq",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 132,
        "name": "Optio dolore itaque",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 133,
        "name": "Libero saepe accusantium",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 134,
        "name": "Illum nequ",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 135,
        "name": "Culpa accusantium fugit id",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 136,
        "name": "Fugit pariatur vero nesciu",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 137,
        "name": "Numqu",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 138,
        "name": "Corrupti sit at cum",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 139,
        "name": "Est fugit incidunt co",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 140,
        "name": "Quos nihil quibusdam",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 141,
        "name": "Sit quidem tempora doloribus r",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 142,
        "name": "Amet vel distinctio mo",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 143,
        "name": "Illum eaque atque recusand",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 144,
        "name": "Dignissi",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 145,
        "name": "Corporis fug",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 146,
        "name": "Sequi nesciunt",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 147,
        "name": "Facere neque qu",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 148,
        "name": "Corporis voluptas provi",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 149,
        "name": "Repella",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 150,
        "name": "Culpa cumque quo vel",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 151,
        "name": "Magni totam q",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 152,
        "name": "Illu",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 153,
        "name": "Sit quibusdam ab, enim in ex",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 154,
        "name": "Consequuntur at earum d",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 155,
        "name": "Voluptatum doloremque to",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 156,
        "name": "Expedita nam est in l",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 157,
        "name": "Repelle",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 158,
        "name": "Sit numqu",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 159,
        "name": "Ipsum sit praesentium cum ame",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 160,
        "name": "Totam delectus sed fugiat o",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 161,
        "name": "Doloremq",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 162,
        "name": "Id reprehenderit ullam rat",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 163,
        "name": "Dignissimos dolo",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 164,
        "name": "Inventore re",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 165,
        "name": "Nemo expl",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 166,
        "name": "Distinctio tene",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 167,
        "name": "Recusandae fug",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 168,
        "name": "Officiis illo cum acc",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 169,
        "name": "Repudiandae molestias be",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 170,
        "name": "Iure nob",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 171,
        "name": "Ea dolor exercitation",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 172,
        "name": "Omnis maxime deserunt",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 173,
        "name": "Eum error eveni",
        "value": 0,
        "weight": 0
    },
    {
        "item_id": 174,
        "name": "Atque repudiandae molestiae v",
        "value": 0,
        "weight": 0
    }
]

armory_weapon = [
    {
        "item_ptr_id": 138,
        "power": 0
    },
    {
        "item_ptr_id": 139,
        "power": 0
    },
    {
        "item_ptr_id": 140,
        "power": 0
    },
    {
        "item_ptr_id": 141,
        "power": 0
    },
    {
        "item_ptr_id": 142,
        "power": 0
    },
    {
        "item_ptr_id": 143,
        "power": 0
    },
    {
        "item_ptr_id": 144,
        "power": 0
    },
    {
        "item_ptr_id": 145,
        "power": 0
    },
    {
        "item_ptr_id": 146,
        "power": 0
    },
    {
        "item_ptr_id": 147,
        "power": 0
    },
    {
        "item_ptr_id": 148,
        "power": 0
    },
    {
        "item_ptr_id": 149,
        "power": 0
    },
    {
        "item_ptr_id": 150,
        "power": 0
    },
    {
        "item_ptr_id": 151,
        "power": 0
    },
    {
        "item_ptr_id": 152,
        "power": 0
    },
    {
        "item_ptr_id": 153,
        "power": 0
    },
    {
        "item_ptr_id": 154,
        "power": 0
    },
    {
        "item_ptr_id": 155,
        "power": 0
    },
    {
        "item_ptr_id": 156,
        "power": 0
    },
    {
        "item_ptr_id": 157,
        "power": 0
    },
    {
        "item_ptr_id": 158,
        "power": 0
    },
    {
        "item_ptr_id": 159,
        "power": 0
    },
    {
        "item_ptr_id": 160,
        "power": 0
    },
    {
        "item_ptr_id": 161,
        "power": 0
    },
    {
        "item_ptr_id": 162,
        "power": 0
    },
    {
        "item_ptr_id": 163,
        "power": 0
    },
    {
        "item_ptr_id": 164,
        "power": 0
    },
    {
        "item_ptr_id": 165,
        "power": 0
    },
    {
        "item_ptr_id": 166,
        "power": 0
    },
    {
        "item_ptr_id": 167,
        "power": 0
    },
    {
        "item_ptr_id": 168,
        "power": 0
    },
    {
        "item_ptr_id": 169,
        "power": 0
    },
    {
        "item_ptr_id": 170,
        "power": 0
    },
    {
        "item_ptr_id": 171,
        "power": 0
    },
    {
        "item_ptr_id": 172,
        "power": 0
    },
    {
        "item_ptr_id": 173,
        "power": 0
    },
    {
        "item_ptr_id": 174,
        "power": 0
    }
]


# for i in range(len(armory_weapon)):
#   db.test.insert_one(armory_weapon[i])

print(db.test.count())

print(list(db.test.find({'item_id': 10})))

def item_finder(item_id, var):
   found = list(db.test.find({item_id:var}))
   print(found)
