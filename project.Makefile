## Add your own custom Makefile targets here

RUN = poetry run

mini_test/mini_schema_generated.yaml: mini_test/mini_schema.yaml
	$(RUN) gen-linkml \
		--output $@ \
		--no-materialize-attributes \
		--format yaml $<

mini_test/mini_data.json: mini_test/mini_schema_generated.yaml mini_test/mini_data.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class Project \
		--schema $^


mini_test/mini_data.ttl: mini_test/mini_schema_generated.yaml mini_test/mini_data.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class Project \
		--schema $^
