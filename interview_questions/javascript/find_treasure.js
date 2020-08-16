/**
 * Rely on ascii conversion of capital letters to 1 - 26
 * Assuming 'A' === 1.
 */
const charToOrd = (character) => character.charCodeAt(0) - 64;

/**
 * Convert string coordinates into distinct parse [row, col] values.
 * Assumes a square with maximum area of 26 * 26
 * @example 1A -> [1,1]
 * @example 20C -> [20,3]
 */
const parseCoordinatePair = (string) => {
  const row = parseInt(string.substring(0, string.length - 1));
  const column = charToOrd(string[string.length - 1]);
  return [row, column];
};

/**
 * Convert array of string coordinates into array of array coordinates.
 * @example 2B 2D 3D 4D 4A -> [[2,2], [2,4], [3,4], [4,4], [4,1]]
 */
const parseCoordinatePairs = (string) => string.split(/\s/).map(parseCoordinatePair);

/**
 * Generate treasure from topLeftBounds and bottomRightBounds
 */
class Treasure {
  constructor([startRow, startCol], [endRow, endCol]) {
    this.startRow = startRow;
    this.endRow = endRow;
    this.startCol = startCol;
    this.endCol = endCol;

    this.areaSize = (endRow - startRow) * (endCol - startCol);
    this.count = 0;
  }

  isWithinRange(row, col) {
    return (row >= this.startRow && row <= this.endRow) && (col >= this.startCol && col <= this.endCol);
  }

  foundPiece() {
    this.count = this.count + 1;
  }

  searchCoordinate(row, col) {
    if (this.isWithinRange(row, col)) {
      this.foundPiece();
      return true;
    }
    return false;
  }

  isComplete() {
    return this.areaSize === this.count;
  }
}

/**
 * Solution.
 * @param {integer} n - guaranteed to be < 26.
 * @param {String} treasures - coordinate ranges separeted by spaces.
 * @param {String} searched - coordinates separated by spaces.
 */
const solution = (
  n,
  treasures,
  searched,
) => {
  let complete = 0;
  let incomplete = 0;

  const treasureCoordinates = treasures
    .split(/,\s*/) // separate by comma
    .map(parseCoordinatePairs); // break out treasure coordinates

  const treasureObjects = treasureCoordinates.map(([topLeft, bottomRight]) => new Treasure(topLeft, bottomRight));
  const searchedCoordinates = parseCoordinatePairs(searched)

  searchedCoordinates.forEach(
    ([row, col]) => treasureObjects.forEach(treasure => treasure.searchCoordinate(row, col))
  );

  treasureObjects.forEach(treasure => treasure.isComplete() ? complete++ : incomplete++);

  return [complete, incomplete];
};

const sampleN = 4;
const sampleTreasures = '1B 2C,2D 4D';
const sampleSearched = '2B 2D 3D 4D 4A';

const testCase = solution(
  sampleN,
  sampleTreasures,
  sampleSearched,
);

console.log(testCase);
