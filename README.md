# kafka-test
An example of application using Kafka with Python

# Test Commands
1) docker-compose exec kafka kafka-topics --create --topic meu-topico-legal --partitions 1 --replication-factor 1 --if-not-exists --zookeeper localhost:32181
2) docker-compose exec kafka kafka-topics --describe --topic meu-topico-legal --zookeeper localhost:32181
3) docker-compose exec kafka bash -c "seq 100 | kafka-console-producer --request-required-acks 1 --broker-list localhost:29092 --topic meu-topico-legal && echo 'Produced 100 messages.'"
4) docker-compose exec kafka kafka-console-consumer --bootstrap-server localhost:29092 --topic meu-topico-legal --from-beginning --max-messages 100
5) docker-compose exec kafka kafka-run-class kafka.admin.ConsumerGroupCommand --all-groups     --bootstrap-server localhost:29092     --describe