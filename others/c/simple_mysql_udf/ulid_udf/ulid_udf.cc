/*
 *
 ** Test
 * mysql> SELECT ULID([ms]);
 * mysql> CREATE TABLE t (id BINARY(16) PRIMARY KEY, name VARCHAR(10) NOT NULL);
 * mysql> INSERT INTO t VALUES (ULID(), "Alice"), (ULID(), "Bob"), (ULID(), "Charlie");
 *
 */

#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <mysql.h> 
#include <mysql/plugin.h>

#define _MSC_VER 0  // Silence a VS Code warning in ulid.hh

#define ULID_BINARY_LENGTH 16

#include "ulid/src/ulid.hh"

namespace ulid_udf {

/**
 * https://dev.mysql.com/doc/extending-mysql/8.0/en/adding-loadable-function.html
 *
 * When an SQL statement invokes XXX(), MySQL calls the initialization function xxx_init() 
 * to let it perform any required setup, such as argument checking or memory allocation. 
 *
 * If xxx_init() returns an error, MySQL aborts the SQL statement with an error message 
 * and does not call the main or deinitialization functions. Otherwise, MySQL calls the 
 * main function xxx() once for each row.
 * 
 * After all rows have been processed, MySQL calls the deinitialization function xxx_deinit() 
 * so that it can perform any required cleanup.
 */

/*
 * Init
 */
extern "C" bool ulid_init(UDF_INIT *initid, UDF_ARGS *args, char *message) {

	if (args->arg_count > 1) {
		strcpy(message, "ULID takes 0 or 1 arguments");
		return true;
	}

	if (args->arg_count == 1 && args->arg_type[0] != INT_RESULT) {
		strcpy(message, "Argument 1 must be an integer representing milliseconds");
		return true;
	}

	initid->max_length = ULID_BINARY_LENGTH;

	return false;
}


/*
 * Main - returns binary ULID
 */
//extern "C" char *ulid(UDF_INIT *initid [[maybe_unused]], UDF_ARGS *args, char *result,
extern "C" char *ulid(UDF_INIT *initid, UDF_ARGS *args, char *result,
		unsigned long *length, unsigned char *is_null,
		unsigned char *error) {

	*is_null = 0;

	ulid::ULID my_ulid = 0;

	if (args->arg_count == 0) {

		// Create a ULID using the current time (std::chrono) in nanoseconds
		ulid::EncodeTimeSystemClockNow(my_ulid);
	}
	else if (args->arg_count == 1) {

		// milliseconds
		long long ms_seed;
		ms_seed = *((long long*) args->args[0]);

		// Encode the provided timestamp
		//std::chrono::system_clock::time_point tp{std::chrono::milliseconds{ms_seed}};
		ulid::EncodeTime(ms_seed, my_ulid);
	}
	else {
		*error = 1;
		return result;
	}

	// Add randomness
	ulid::EncodeEntropyRand(my_ulid);

	// Marshal ulid to binary array
	uint8_t dst[16];
	ulid::MarshalBinaryTo(my_ulid, dst);

	// Copy binary array to mysql result pointer and confirm length
	memcpy(result, dst, ULID_BINARY_LENGTH);
	*length = ULID_BINARY_LENGTH;

	return result;
}


/**
 * De-init - cleanup memory allocated during init
 */
extern "C" void ulid_deinit(UDF_INIT *initid) {}

} // namespace ulid_udf
