// Get the API base URL from environment or fallback to localhost (no trailing slash)
const API_BASE_URL =
  (process.env.NEXT_PUBLIC_API_URL?.replace(/\/$/, "")) || "http://localhost:8000";

console.log("✅ API_BASE_URL is:", API_BASE_URL);

// -------------------- Interfaces --------------------
export interface Product {
  id: number;
  name: string;
  category_id?: number;
}

export interface Category {
  id: number;
  name: string;
}

export interface Retailer {
  id: number;
  name: string;
}

export interface Price {
  id: number;
  product_id: number;
  retailer_id: number;
  price: number;
  timestamp: string;
}

export interface Alert {
  id: number;
  item_id: number;
  store_id: number;
  price_change: number;
  direction: string;
  threshold: number;
  timestamp: string;
  description: string;
}

export interface ForecastResponse {
  product_id: number;
  forecast_price: number;
  based_on_last_days: number;
}

// -------------------- API Client --------------------
class ApiClient {
  private async request<T>(endpoint: string): Promise<T> {
    const fullUrl = `${API_BASE_URL}${endpoint}`;
    console.log("🔄 Fetching from:", fullUrl);

    try {
      const response = await fetch(fullUrl, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        console.error("❌ API Error:", response.statusText, "from", fullUrl);
        throw new Error(`API Error: ${response.statusText}`);
      }

      return response.json();
    } catch (error) {
      console.error("🚨 Fetch failed:", error);
      throw error;
    }
  }

  async getProducts(): Promise<Product[]> {
    return this.request<Product[]>("/api/v1/products/");
  }

  async getCategories(): Promise<Category[]> {
    return this.request<Category[]>("/api/v1/categories/");
  }

  async getRetailers(): Promise<Retailer[]> {
    return this.request<Retailer[]>("/api/v1/retailers/");
  }

  async getPrices(): Promise<Price[]> {
    return this.request<Price[]>("/api/v1/prices/");
  }

  async getForecast(productId: number): Promise<ForecastResponse> {
    return this.request<ForecastResponse>(
      `/api/v1/forecast/?product_id=${productId}`
    );
  }
}

export const apiClient = new ApiClient();



