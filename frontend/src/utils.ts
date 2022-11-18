export const API_URL_Generator = (url: string) => {
    const BASE_PATH = process.env.ENV === "DEV" ? "http://localhost:8000": "";
    return BASE_PATH + url
};