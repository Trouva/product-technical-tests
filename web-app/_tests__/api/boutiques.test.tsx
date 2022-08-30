import axios from 'axios';
import { createMocks } from 'node-mocks-http';
import { boutiques } from '../../mock/boutiques';
import { boutiques as APIBoutique } from '../../mock/api/boutiques';
import handle from '../../pages/api/boutiques';

jest.mock("axios");
const mockedAxios = axios as jest.Mocked<typeof axios>;

describe('/api/[boutiques]', () => {
  test('returns a message with close boutiques', async () => {
    mockedAxios.get.mockResolvedValueOnce({data: APIBoutique});

    const { req, res } = createMocks({
      method: 'GET',
      query: { lon: -2.3178781, lat: 53.6480779 },
    },);

    await handle(req, res);

    expect(res._getStatusCode()).toBe(200);
    expect(JSON.parse(res._getData())).toEqual(boutiques);
  });
});