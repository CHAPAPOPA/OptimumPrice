import scrapy


class RealEstateSpider(scrapy.Spider):
    name = "real_estate_spider"
    allowed_domains = ["xn--80az8a.xn--d1aqf.xn--p1ai"]
    start_urls = [
        "https://xn--80az8a.xn--d1aqf.xn--p1ai/сервисы/каталог-новостроек/список-объектов/"
        + "список?objStatus=0&place=0-44"
    ]

    def parse(self, response):
        """Парсер основной информации с каждой карточки объекта"""
        with open("debug.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        items = response.xpath('//div[@class="catalog-item"]')
        print(f"Found {len(items)} items on page.")
        for item in items:
            title = item.xpath(".//h2/text()").get()
            print(f"Processing item: {title}")

            data = {
                "title": item.xpath(".//h2/text()").get(),
                "address": item.xpath('.//div[@class="address"]/text()').get(),
                "id": item.xpath(".//@data-id").get(),
                "commissioning_date": item.xpath(
                    './/div[@class="commissioning-date"]/text()'
                ).get(),
                "developer": item.xpath('.//div[@class="developer"]/text()').get(),
            }

            details_url = item.xpath(".//a/@href").get()
            if details_url:
                yield response.follow(
                    details_url, self.parse_details, meta={"data": data}
                )

        next_page = response.xpath(
            '//button[@class="show-more-button"]/@data-next-url'
        ).get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_details(self, response):
        """Получаем данные, которые были переданы из метода parse"""
        data = response.meta["data"]

        data.update(
            {
                "group": response.xpath('//div[@class="group"]/text()').get(),
                "publish_date": response.xpath(
                    '//div[@class="publish-date"]/text()'
                ).get(),
                "handover_date": response.xpath(
                    '//div[@class="handover-date"]/text()'
                ).get(),
                "price_per_sq_m": response.xpath(
                    '//div[@class="price-per-sq-m"]/text()'
                ).get(),
                "sold_out_percentage": response.xpath(
                    '//div[@class="sold-out-percentage"]/text()'
                ).get(),
                "property_class": response.xpath(
                    '//div[@class="property-class"]/text()'
                ).get(),
                "total_apartments": response.xpath(
                    '//div[@class="total-apartments"]/text()'
                ).get(),
            }
        )

        yield data
