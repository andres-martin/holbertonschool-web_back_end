const { default: createReportObject } = require("./12-createReportObject");

test('loop', () => {
    expect(createReportObject([
        'John Doe',
        'Guillaume Salva',
    ])).toStrictEqual({
        allEmployees: {
            engineering: [
                'John Doe',
                'Guillaume Salva',
            ],
        },
    });
});
