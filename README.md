# wisdom

Generates random wisdom quote using an API.

## Example

By default prints out one quote.

``All wrong-doing arises because of mind. If mind is transformed can wrong-doing remain?   - Buddha``

You can use env variable QUOTES to change the amount of quotes return, the maximum is 5. For example QUOTES=2 returns 2 quotes.

## Usage

```
python app.py
```

### Docker

```
docker build -t random-quote .

docker run -it -e QUOTES=2 random-quote
```
