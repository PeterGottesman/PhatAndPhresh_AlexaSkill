#!/bin/python3

import phat_lambda

event = {
      "session": {
              "new": False,
              "sessionId": "SessionId.2f3223a8-407e-4b85-93f6-42b186acabe2",
              "application": {
                        "applicationId": "amzn1.ask.skill.0a11af58-1379-4432-a382-8dd19e779029"
                      },
              "attributes": {},
              "user": {
                        "userId": "amzn1.ask.account.AFMADHDL5NP4DUZFZ4KSYTRHXD3TRZSO25KSIKPCRIHQUKOA6MFCFDUZNEOSJYHBT22VC4WT27RH43COUYCV62IYAML6NFI5VMM757GNWQWKPN6DETCOIG5GCXJIFXE63OMKJNIXRX2PBXPUSWY4KW2O5HN33POGGCTBJPHTBRL6I67QCPNXSLZOWOBDASLEB32PMSOD6A4B36A"
                      }
            },
      "request": {
              "type": "IntentRequest",
              "requestId": "EdwRequestId.de0ab25a-7f3c-4df6-b6c0-15a4bbbc34b7",
              "intent": {
                        "name": "PhireIntent",
                        "slots": {
                                    "num_verses": {
                                                  "name": "num_verses",
                                                  "value": "5"
                                                }
                                  }
                      },
              "locale": "en-US",
              "timestamp": "2017-10-07T22:53:44Z"
            },
      "context": {
              "AudioPlayer": {
                        "playerActivity": "IDLE"
                      },
              "System": {
                        "application": {
                                    "applicationId": "amzn1.ask.skill.0a11af58-1379-4432-a382-8dd19e779029"
                                  },
                        "user": {
                                    "userId": "amzn1.ask.account.AFMADHDL5NP4DUZFZ4KSYTRHXD3TRZSO25KSIKPCRIHQUKOA6MFCFDUZNEOSJYHBT22VC4WT27RH43COUYCV62IYAML6NFI5VMM757GNWQWKPN6DETCOIG5GCXJIFXE63OMKJNIXRX2PBXPUSWY4KW2O5HN33POGGCTBJPHTBRL6I67QCPNXSLZOWOBDASLEB32PMSOD6A4B36A"
                                  },
                        "device": {
                                    "supportedInterfaces": {}
                                  }
                      }
            },
      "version": "1.0"
    }

print(phat_lambda.phat_handler(event, None))
