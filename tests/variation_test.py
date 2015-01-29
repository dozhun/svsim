from svsim.variation import *

##
# Tests basic properties of the Insertion object.
#
def test_insertion():
    insertion = Insertion( 2, 5, -1 )
    assert len( insertion.get_sequence( "" ) ) == 5
    assert insertion.get_delta( ) == 0

    insertion = Insertion( 2, 2, 4 )
    assert insertion.get_sequence( "ABCDEFGH" ) == "EF"

##
# Tests basic properties of the Deletion object.
#
def test_deletion():
    deletion = Deletion( 2, 5 )
    assert deletion.get_sequence( "ABCDEFGH" ) == []
    assert deletion.get_delta( ) == 5

##
# Tests basic properties of the Null object.
#
def test_null():
    null = NullVariation( 2, 2 )
    assert null.get_sequence( "ABCDEFGHIJ" ) == "CD"
    assert null.get_delta( ) == 2

##
# Tests that the reference genome is chunked properly.
#
# Insertion
# Reference: 123456789AB
# Donor:     12AB3456789AB
#
# Deletion
# Reference: 123456789AB
# Donor:     1236789
#
def test_create_chunks():
    genome = "123456789AB"
    variations = [ Insertion( 1, 2, 9 ) ]
    chunks = create_chunks( variations, len( genome ) )

    assert len( chunks ) == 3

    assert chunks[ 0 ].get_sequence( genome ) == "12"
    assert chunks[ 1 ].get_sequence( genome ) == "AB"
    assert chunks[ 2 ].get_sequence( genome ) == "3456789AB"

    variations = [ Deletion( 2, 2 ) ]

    chunks = create_chunks( variations, len( genome ) )
    
    assert len( chunks ) == 3
    assert chunks[ 0 ].get_sequence( genome ) == "123"
    assert chunks[ 1 ].get_sequence( genome ) == []
    assert chunks[ 2 ].get_sequence( genome ) == "6789AB"