FLAGS=


run:
	uvicorn src.app:app --reload

clean:
	chmod +x scripts/cleanup.sh
	. scripts/cleanup.sh

tests:
	chmod +x scripts/tests.sh
	. scripts/tests.sh
	make clean
