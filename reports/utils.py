URL = "https://my.geotab.com/apiv1"

EXCEPTIONS_BODY = {
    "method": "Get",
    "params": {
        "typeName": "Trip",
        "credentials": {
            "database": "moove",
            "sessionId": "2nR_L-I6A8F0K5DVF8srFQ",
            "userName": "moovechallengeuser@mooveconnected.com"
        },
        # TODO : Make an auto 30 days check.
        "search": {
            "fromDate": "2022-08-14T22:00:00.000Z",
            "toDate": "2022-08-22T22:00:00.000Z"
        }
    }
}

TRIPS_BODY = {
    "method": "Get",
    "params": {
        "typeName": "ExceptionEvent",
        "credentials": {
            "database": "moove",
            "sessionId": "2nR_L-I6A8F0K5DVF8srFQ",
            "userName": "moovechallengeuser@mooveconnected.com"
        },
        # TODO : Make an auto 30 days check.
        "search": {
            "fromDate": "2022-08-14T22:00:00.000Z",
            "toDate": "2022-08-22T22:00:00.000Z"
        }
    }
}

VEHICLE_BODY = {
    "method": "Get",
    "params": {
        "typeName": "Device",
        "credentials": {
            "database": "moove",
            "sessionId": "2nR_L-I6A8F0K5DVF8srFQ",
            "userName": "moovechallengeuser@mooveconnected.com"
        }
    }
}

HARSH_ACCELERATION = 'apUro_0nXOUmLV4SVlzK8Xw'
SPEEDING = 'abHSbCv2PKUWKSSGJMoiBnQ'
