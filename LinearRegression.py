import pandas as pd
import torch
import torch_directml
from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler, RobustScaler

class FeatureScalingCpu(object):
    def __init__(self, feature_scaling, csv_path) -> None:
        self.feature_scaling_method = feature_scaling
        self.data = self.load_data(csv_path)

    @staticmethod
    def load_data(csv_path):
        try:
            data = pd.read_csv(csv_path, encoding='utf-8')
            return data
        except Exception as e:
            raise ValueError(f"加载数据失败: {e}")

    def feature_scaling(self):
        if self.feature_scaling_method == "min-max_normalization":
            return self.__min_max_normalization()
        elif self.feature_scaling_method == "mean_normalization":
            return self.__mean_normalization()
        elif self.feature_scaling_method == "z-score_normalization":
            return self.__z_score_normalization()
        elif self.feature_scaling_method == "max_abs_normalization":
            return self.__max_abs_normalization()
        elif self.feature_scaling_method == "robust_standardization":
            return self.__robust_standardization()
        else:
            raise ValueError("不支持的特征缩放方法")

    def __min_max_normalization(self):
        scaler_object = MinMaxScaler()
        return pd.DataFrame(scaler_object.fit_transform(self.data), columns=self.data.columns)

    def __mean_normalization(self):
        scaler_object = MinMaxScaler()
        scaler_object_data = pd.DataFrame(scaler_object.fit_transform(self.data), columns=self.data.columns)
        return scaler_object_data - scaler_object_data.mean()

    def __z_score_normalization(self):
        scaler_object = StandardScaler()
        return pd.DataFrame(scaler_object.fit_transform(self.data), columns=self.data.columns)

    def __max_abs_normalization(self):
        scaler_object = MaxAbsScaler()
        return pd.DataFrame(scaler_object.fit_transform(self.data), columns=self.data.columns)

    def __robust_standardization(self):
        scaler_object = RobustScaler()
        return pd.DataFrame(scaler_object.fit_transform(self.data), columns=self.data.columns)

class FeatureScalingGpu(FeatureScalingCpu):
    def __init__(self, feature_scaling, csv_path) -> None:
        super().__init__(feature_scaling, csv_path)
        self.device = self.__get_device()

    def __get_device(self):
        if torch.cuda.is_available():
            return torch.device('cuda')
        else:
            return torch_directml.device()

    def __to_tensor(self, data):
        return torch.tensor(data.values, dtype=torch.float32, device=self.device)

    def __min_max_normalization(self):
        data_tensor = self.__to_tensor(self.data)
        min_vals = data_tensor.min(dim=0, keepdim=True)[0]
        max_vals = data_tensor.max(dim=0, keepdim=True)[0]
        scaled_tensor = (data_tensor - min_vals) / (max_vals - min_vals)
        return pd.DataFrame(scaled_tensor.cpu().numpy(), columns=self.data.columns)

    def __mean_normalization(self):
        data_tensor = self.__to_tensor(self.data)
        min_vals = data_tensor.min(dim=0, keepdim=True)[0]
        max_vals = data_tensor.max(dim=0, keepdim=True)[0]
        mean_vals = data_tensor.mean(dim=0, keepdim=True)
        scaled_tensor = (data_tensor - mean_vals) / (max_vals - min_vals)
        return pd.DataFrame(scaled_tensor.cpu().numpy(), columns=self.data.columns)

    def __z_score_normalization(self):
        data_tensor = self.__to_tensor(self.data)
        mean_vals = data_tensor.mean(dim=0, keepdim=True)
        std_vals = data_tensor.std(dim=0, keepdim=True)
        scaled_tensor = (data_tensor - mean_vals) / std_vals
        return pd.DataFrame(scaled_tensor.cpu().numpy(), columns=self.data.columns)

    def __max_abs_normalization(self):
        data_tensor = self.__to_tensor(self.data)
        max_vals = data_tensor.abs().max(dim=0, keepdim=True)[0]
        scaled_tensor = data_tensor / max_vals
        return pd.DataFrame(scaled_tensor.cpu().numpy(), columns=self.data.columns)

    def __robust_standardization(self):
        data_tensor = self.__to_tensor(self.data)
        median_vals = data_tensor.median(dim=0, keepdim=True)[0]
        q1_vals = torch.quantile(data_tensor, 0.25, dim=0, keepdim=True)
        q3_vals = torch.quantile(data_tensor, 0.75, dim=0, keepdim=True)
        scaled_tensor = (data_tensor - median_vals) / (q3_vals - q1_vals)
        return pd.DataFrame(scaled_tensor.cpu().numpy(), columns=self.data.columns)


class LinearRegression(object):
    pass
    #def __init__(self):
        #self.gradient_descent

path = r"D:\桌面\Lightweight_notepad\啊.csv"
scaler = FeatureScalingCpu("mean_normalization", path)
scaled_data = scaler.feature_scaling()
print(scaled_data)
