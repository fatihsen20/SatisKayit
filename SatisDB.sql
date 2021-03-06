CREATE DATABASE [Satis]
GO
/****** Object:  Table [dbo].[tbl_Aksesuar]    Script Date: 28.06.2022 14:21:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_Aksesuar](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Ad] [nvarchar](50) NOT NULL,
	[AlisFiyati] [int] NOT NULL,
 CONSTRAINT [PK_tbl_Aksesuar] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tbl_AksesuarSatis]    Script Date: 28.06.2022 14:21:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_AksesuarSatis](
	[Aksesuar_Id] [int] NOT NULL,
	[Aksesuar_Adi] [nvarchar](50) NOT NULL,
	[Tarih] [nvarchar](50) NOT NULL,
	[Aksesuar_Satis] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tbl_Alim]    Script Date: 28.06.2022 14:21:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_Alim](
	[UrunId] [int] IDENTITY(1,1) NOT NULL,
	[IMEI] [nvarchar](50) NOT NULL,
	[Marka] [nvarchar](50) NULL,
	[AlimTarihi] [date] NULL,
	[AlimFiyati] [int] NULL,
	[AlimYeri] [nvarchar](50) NULL,
 CONSTRAINT [PK_tbl_Alim] PRIMARY KEY CLUSTERED 
(
	[UrunId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tbl_Gider]    Script Date: 28.06.2022 14:21:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_Gider](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Tarih] [date] NULL,
	[GiderAdi] [nvarchar](50) NULL,
	[GiderMiktari] [int] NOT NULL,
 CONSTRAINT [PK_tbl_Gider] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tbl_Satis]    Script Date: 28.06.2022 14:21:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_Satis](
	[Urun_Id] [int] NOT NULL,
	[Urun] [nvarchar](50) NOT NULL,
	[IMEI] [nvarchar](50) NOT NULL,
	[Tarih] [date] NOT NULL,
	[Satis_Fiyati] [int] NOT NULL,
 CONSTRAINT [PK_tbl_Satis] PRIMARY KEY CLUSTERED 
(
	[Urun_Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tbl_TeknikServis]    Script Date: 28.06.2022 14:21:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_TeknikServis](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Tarih] [date] NOT NULL,
	[Islem] [nvarchar](50) NOT NULL,
	[Tutar] [int] NOT NULL,
	[Maliyet] [int] NOT NULL,
 CONSTRAINT [PK_tbl_TeknikServis] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[tbl_AksesuarSatis]  WITH CHECK ADD  CONSTRAINT [FK_tbl_AksesuarSatis_tbl_Aksesuar] FOREIGN KEY([Aksesuar_Id])
REFERENCES [dbo].[tbl_Aksesuar] ([ID])
GO
ALTER TABLE [dbo].[tbl_AksesuarSatis] CHECK CONSTRAINT [FK_tbl_AksesuarSatis_tbl_Aksesuar]
GO
ALTER TABLE [dbo].[tbl_Satis]  WITH CHECK ADD  CONSTRAINT [FK_tbl_Satis_tbl_Alim] FOREIGN KEY([Urun_Id])
REFERENCES [dbo].[tbl_Alim] ([UrunId])
GO
ALTER TABLE [dbo].[tbl_Satis] CHECK CONSTRAINT [FK_tbl_Satis_tbl_Alim]
GO
