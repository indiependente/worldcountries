<?php
$tz = timezone_identifiers_list();
function get_timezone_abbreviation($timezone_id)
{
	if($timezone_id){
		$abb_list = timezone_abbreviations_list();
		$abb_array = array();
		foreach ($abb_list as $abb_key => $abb_val) {
			foreach ($abb_val as $key => $value) {
				$value['abb'] = $abb_key;
				array_push($abb_array, $value);
			}
		}
		foreach ($abb_array as $key => $value) {
			if($value['timezone_id'] == $timezone_id){
				return strtoupper($value['abb']);
			}
		}
	}
	return FALSE;
}

function ch150918__utc_offset_dst( $time_zone ) {
	// Set UTC as default time zone.
	date_default_timezone_set( 'UTC' );
	$utc = new DateTime();
	// Calculate offset.
	$current   = timezone_open( $time_zone );
	$offset_s  = timezone_offset_get( $current, $utc ); // seconds
	$offset_h  = $offset_s / ( 60 * 60 ); // hours
	// Prepend “+” when positive
	$offset_h  = (string) $offset_h;
	
	if ( strpos( $offset_h, '.' ) === FALSE ) {
		$offset_h .= ':00';
	}
	else {
		if ( strpos( $offset_h, '.5' ) ) {
			$offset_h = str_replace('.5', ':30', $offset_h);
		}
		else if ( strpos( $offset_h, '.75' )  ) {
			$offset_h = str_replace('.75', ':45', $offset_h);
		}
	}

	if ( strpos( $offset_h, '-' ) === FALSE ) {
		$offset_h = '+' . $offset_h; // prepend +
	}
	return 'UTC ' . $offset_h;
}

$dateTimeZoneUTC= new DateTimeZone("UTC");

foreach ($tz as $k => $v)
{
	$dateTimeZoneV = new DateTimeZone($v);
	echo $v.', '.get_timezone_abbreviation($v).', '.ch150918__utc_offset_dst($v)."\n";
}

?>