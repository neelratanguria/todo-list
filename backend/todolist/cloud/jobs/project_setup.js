Parse.Cloud.job("projectSetup", (request) => {
    // create an instance to manage your class
    const mySchema = new Parse.Schema('MyClass');

    // gets the current schema data
    mySchema.get();

    // returns schema for all classes
    Parse.Schema.all()

    // add any # of fields, without having to create any objects
    mySchema
        .addString('stringField')
        .addNumber('numberField')
        .addBoolean('booleanField')
        .addDate('dateField')
        .addFile('fileField')
        .addGeoPoint('geoPointField')
        .addPolygon('polygonField')
        .addArray('arrayField')
        .addObject('objectField')
        .addPointer('pointerField', '_User')
        .addRelation('relationField', '_User');

    // new types can be added as they are available
    mySchema.addField('newField', 'ANewDataType')

    // save/update this schema to persist your field changes
    mySchema.save().then((result) => {
        // returns save new schema
    });
    // or
    mySchema.update().then((result) => {
        // updates existing schema
    });
});