.PHONY: run
run:
	@python3.10 $(filter-out $@,$(MAKECMDGOALS))