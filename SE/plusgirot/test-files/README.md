# Plusgirot


## Send

| MessageType | System                    | Description                               | Link                                              |
| ----------- | ------------------------- | ----------------------------------------- | ------------------------------------------------- |
| A05         | AUTOGIRO                  | Inrapportering av Betalningsuppdrag       | [pg_testfil_a05_s.txt](send/pg_testfil_a05_s.txt) |
| 01P         | FAKTURABETALNINGSSERVICE  | Inrapportering av Betalningsunderlag      | [pg_testfil_01p_s.txt](send/pg_testfil_01p_s.txt) |
| PO1         | GIROVISIONSBETALNINGAR    | Betalningar GiroVision                    | [pg_testfil_po1_s.txt](send/pg_testfil_po1_s.txt) |





## Receive 

| MessageType | System                    | Description                                                 | Link                                                 |
| ----------- | ------------------------- | ----------------------------------------------------------- | ---------------------------------------------------- |
| A04         | AUTOGIRO                  | Redovisning av Betalningsuppdrag                            | [pg_testfil_a04_h.txt](receive/pg_testfil_a04_h.txt) |
| 12P         | FAKTURABETALNINGSSERVICE  | Redovisning av Beordrade betalningar                        | [pg_testfil_12p_h.txt](receive/pg_testfil_12p_h.txt) |
| CR1         | GIROVISIONSBETALNINGAR    | Krediteringsbesked                                          | [pg_testfil_cr1_h.txt](receive/pg_testfil_cr1_h.txt) |
| DA1         | GIROVISIONSBETALNINGAR    | Debiteringsbesked                                           | [pg_testfil_da1_h.txt](receive/pg_testfil_da1_h.txt) |
| POR         | GIROVISIONSBETALNINGAR    | Återrapportering av Felaktiga betalningar                   | [pg_testfil_por_h.txt](receive/pg_testfil_por_h.txt) |
| 02P         | INBETALNINGSSERVICE       | Sammanställning av Inkommande betalningar                   | [pg_testfil_02p_h.txt](receive/pg_testfil_02p_h.txt) |
| 24P         | TIPS                      | Redovisning av betalningar från Fakturabetalningsservice    | [pg_testfil_24p_h.txt](receive/pg_testfil_24p_h.txt) |


